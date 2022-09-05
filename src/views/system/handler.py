from sanic import Blueprint

from auth import login_required
from authorization import level_required
from models.system import System

blue = Blueprint(__name__, url_prefix='/')


@blue.post("create")
@login_required
async def create_system(request):
    session = request.ctx.session
    return await System.insert(request.json, session=session)


@blue.post("creates")
@login_required
async def create_systems(request):
    session = request.ctx.session
    return await System.insert_batch(request.json, session=session)


@blue.post("delete")
@login_required
@level_required(3)
async def delete_systems(request):
    session = request.ctx.session
    return await System.delete_batch(request.json, session)


@blue.delete("delete/<pk:int>")
@login_required
@level_required(3)
async def delete_system(request, pk):
    session = request.ctx.session
    return await System.delete_by_id(pk, session=session)


@blue.get("get/<pk:int>")
@login_required
async def get_system(request, pk):
    session = request.ctx.session
    return await System.read_one_by_id(pk, session)


@blue.get("get")
@login_required
@level_required(3)
async def get_systems(request):
    session = request.ctx.session
    return await System.read_all(session)


@blue.get("page")
@login_required
async def page(request):
    session = request.ctx.session
    return await System.read_all_pagination(request.args, session=session)


@blue.post("update/<pk:int>")
@login_required
async def update_system(request, pk):
    session = request.ctx.session
    return await System.update(pk, request.json, session)
