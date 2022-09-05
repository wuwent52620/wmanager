import os

import aiofiles
import jwt
from sanic import Blueprint, json, text, response
from sqlalchemy import select

from auth import login_required, w_user, token_data, clean_user
from authorization import level_required
from common.commons import json_response, BaseDir
from models.user import User
from utils.parser import md5

blue = Blueprint(__name__, url_prefix='/')


@blue.post("login")
async def login(request):
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(User).where(User.username == data['username'])
        result = await session.execute(stmt)
        person = result.scalar()

    if not person:
        return json_response(400, data='用户名错误')
    else:
        if md5(data, key='password').get('password') == person.password:
            try:
                w_user.uid = person.id
                w_user.name = person.username
                w_user.level = person.level
                w_user.tid = person.team_id
                token = jwt.encode(payload=token_data(w_user.to_dict()), key=request.app.config.SECRET,
                                   headers=dict(typ="JWT", alg="HS256"), algorithm='HS256')
            except (KeyError, ValueError) as ex:
                raise KeyError(f"request data must contain right info ({ex})")
            return json_response(200, data={'token': token, 'message': 'login success!'})
        else:
            return json_response(400, data='密码错误')


@blue.get("logout")
@login_required
async def logout(request):
    clean_user()
    return text('Logout Successful')


@blue.post("/any_upload")
@login_required
@level_required(3)
async def upload(request):
    file = request.files.get('file')
    _type = os.path.splitext(file.name)
    fn = request.form.get('fn') or 'default'

    name = f"{fn}{_type[1]}"
    path = os.path.join(BaseDir, "Anything")  # 这里注意path是绝对路径
    if not os.path.exists(path):
        os.makedirs(path)
    file_path = os.path.join(path, name)
    if os.path.exists(file_path):
        os.remove(file_path)
    async with aiofiles.open(file_path, 'wb') as f:
        await f.write(file.body)
        f.close()
    return json_response(data={"msg": "上传成功", "name": name})


@blue.get('/any_download/<pt:str>')
async def file(request, pt):
    path = os.path.join(BaseDir, "Anything")
    file_path = os.path.join(path, pt)
    return await response.file(
        file_path
    )
