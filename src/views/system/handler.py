from sanic import json, Blueprint
from sqlalchemy import select

from auth import login_required
from authorization import level_required
from models.system import System

blue = Blueprint(__name__, url_prefix='/')


@blue.post("create")
async def create_system(request):
    session = request.ctx.session
    async with session.begin():
        obj = System(**request.json)
        session.add_all([obj])
    return json(obj.to_dict())


@blue.delete("delete")
async def delete_systems(request):
    session = request.ctx.session
    async with session.begin():
        session.query(System).filter(System.id.in_(*request.json)).delete(synchronize_session=False)
    return json(json(f"delete systems ({request.json}) successful"))


@blue.delete("delete/<pk:int>")
async def delete_system(request, pk):
    session = request.ctx.session
    async with session.begin():
        session.query(System).filter(System.id == pk).delete()
    return json(f"delete system ({pk}) successful")


@blue.get("get/<pk:int>")
@level_required(1)
async def get_system(request, pk):
    session = request.ctx.session
    async with session.begin():
        stmt = select(System).where(System.id == pk)
        result = await session.execute(stmt)
        obj = result.scalar()

    if not obj:
        return json({})

    return json(obj.to_dict())


@blue.get("get")
@level_required(3)
@login_required
async def get_systems(request):
    session = request.ctx.session
    async with session.begin():
        stmt = select(System).filter()
        result = await session.execute(stmt)
        objs = result.fetchall()

    if not objs:
        return json({})

    return json([obj[0].to_dict() for obj in objs])
