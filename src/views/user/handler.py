from sanic import Blueprint, json
from sqlalchemy import select

from auth import login_required
from models.user import User

blue = Blueprint(__name__, url_prefix='/')


@blue.post("create")
@login_required
async def create_user(request):
    session = request.ctx.session
    async with session.begin():
        person = User(**request.json)
        session.add_all([person])
    return json(person.to_dict())


@blue.delete("delete")
@login_required
async def delete_users(request):
    session = request.ctx.session
    async with session.begin():
        session.query(User).filter(User.id.in_(*request.json)).delete(synchronize_session=False)
    return json(json(f"delete users ({request.json}) successful"))


@blue.delete("delete/<pk:int>")
@login_required
async def delete_user(request, pk):
    session = request.ctx.session
    async with session.begin():
        session.query(User).filter(User.id == pk).delete()
    return json(f"delete user ({pk}) successful")


@blue.get("get/<pk:int>")
async def get_user(request, pk):
    session = request.ctx.session
    async with session.begin():
        stmt = select(User).where(User.id == pk)
        result = await session.execute(stmt)
        person = result.scalar()

    if not person:
        return json({})

    return json(person.to_dict())


@blue.get("get")
@login_required
async def get_users(request):
    session = request.ctx.session
    async with session.begin():
        stmt = select(User).filter()
        result = await session.execute(stmt)
        persons = result.fetchall()

    if not persons:
        return json({})

    return json([person[0].to_dict() for person in persons])
