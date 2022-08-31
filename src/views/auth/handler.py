import jwt
from sanic import Blueprint, json, text
from sqlalchemy import select

from auth import login_required, w_user, token_data
from models.user import User

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
        return text('用户名错误', 400)
    else:
        if data['password'] == person.password:
            try:
                w_user.uid = person.id
                w_user.name = person.username
                w_user.level = person.level
                token = jwt.encode(payload=token_data(request.json), key=request.app.config.SECRET,
                                   headers=dict(typ="JWT", alg="HS256"), algorithm='HS256')
            except (KeyError, ValueError) as ex:
                raise KeyError(f"request data must contain right info ({ex})")
            return json({'token': token, 'message': 'login success!'})
        else:
            return text('密码错误', 400)


@blue.get("logout")
@login_required
async def logout(request):
    w_user.uid = -1
    w_user.name = -1
    w_user.level = -1
    return text('Logout Successful')
