import time
from functools import wraps

import jwt
from sanic import text


def check_token(request):
    """ 校验token是否有效 """
    try:
        jwt.decode(request.headers.get('token'), request.app.config.SECRET, algorithms=["HS256"])
    except jwt.exceptions.InvalidTokenError:
        return False
    else:
        return True


def login_required(wrapped):
    """ token校验装饰器 """

    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authenticated = check_token(request)

            if is_authenticated:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return text("token无效, 请重新登录", 401)

        return decorated_function

    return decorator(wrapped)


def token_data(data: dict):
    now_time = int(time.time())
    expire_time = int(time.time()) + 30
    dic = {
        "exp": expire_time,
        "iat": now_time,
        "data": data
    }
    return dic


class User(object):
    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance__:
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__

    def __init__(self, uid, name, level):
        self.uid = uid
        self.name = name
        self.level = level


w_user = User(-1, -1, -1)
