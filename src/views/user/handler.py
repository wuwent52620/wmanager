from sanic import Blueprint

from auth import login_required
from authorization import level_required
from models.user import User
from utils.parser import md5

blue = Blueprint(__name__, url_prefix='/')


@blue.post("create")
@login_required
@level_required(3)
async def create_user(request):
    session = request.ctx.session
    data = request.json
    data = md5(data, key='password')
    return await User.insert(data, session)


@blue.post("creates")
@login_required
@level_required(3)
async def create_users(request):
    session = request.ctx.session
    data = request.json
    data = md5(data, key='password')
    return await User.insert_batch(data, session)


@blue.post("delete")
@login_required
@level_required(3)
async def delete_users(request):
    session = request.ctx.session
    return await User.delete_batch(request.json, session)


@blue.delete("delete/<pk:int>")
@login_required
@level_required(3)
async def delete_user(request, pk):
    session = request.ctx.session
    return await User.delete_by_id(pk, session)


@blue.get("get/<pk:int>")
@login_required
async def get_user(request, pk):
    session = request.ctx.session
    return await User.read_one_by_id(pk, session)


@blue.get("get")
@login_required
@level_required(3)
async def get_users(request):
    session = request.ctx.session
    return await User.read_all(session)


@blue.post("update/<pk:int>")
@login_required
@level_required(3)
async def update_user(request, pk):
    session = request.ctx.session
    data = request.json
    data = md5(data, key='password')
    return await User.update(pk, data, session)
