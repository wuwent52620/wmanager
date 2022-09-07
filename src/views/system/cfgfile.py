import os

import aiofiles
from sanic import Blueprint, response

from auth import login_required
from common.commons import json_response, BaseDir

blue = Blueprint(__name__, url_prefix='/')


@blue.post("upload")
@login_required
async def upload(request):
    allow_type = ['.jpg', '.png', '.xml', '.yaml', '.xlsx', '.txt']  # 允许上传的类型
    file = request.files.get('file')
    _type = os.path.splitext(file.name)
    fn = request.form.get('fn') or 'default'

    if _type[1] not in allow_type:
        return json_response(400, data="只允许上传图片或文本文件")

    name = f"{fn}{_type[1]}"
    path = os.path.join(BaseDir, "static")  # 这里注意path是绝对路径
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join(path, name)
    if os.path.exists(file_path):
        os.remove(file_path)
    async with aiofiles.open(file_path, 'wb') as f:
        await f.write(file.body)
    return json_response(data={"msg": "上传成功", "name": name})


@blue.get('download/<pt:str>')
@login_required
async def file(request, pt):
    path = os.path.join(BaseDir, "static")
    file_path = os.path.join(path, pt)
    return await response.file(
        file_path
    )
