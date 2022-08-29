import time

from sanic import text, Blueprint, json
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models.user import User

blue = Blueprint(__name__, url_prefix='/')


@blue.post("/user")
async def create_user(request):
    session = request.ctx.session
    async with session.begin():
        person = User(name="foo")
        session.add_all([person])
    return json(person.to_dict())


@blue.get("/user/<pk:int>")
async def get_user(request, pk):
    session = request.ctx.session
    async with session.begin():
        stmt = select(User).where(User.id == pk).options(selectinload(User.cars))
        result = await session.execute(stmt)
        person = result.scalar()

    if not person:
        return json({})

    return json(person.to_dict())
