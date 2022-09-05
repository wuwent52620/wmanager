import time
from functools import wraps
from threading import Lock

from sanic import text


def login_required(wrapped):
    """ token校验装饰器 """

    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            user_id = w_user.uid

            if user_id > 0:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return text("token无效, 请重新登录", 401)

        return decorated_function

    return decorator(wrapped)


def token_data(data: dict):
    now_time = int(time.time())
    expire_time = int(time.time()) + 60 * 60 * 24 * 3
    dic = {
        "exp": expire_time,
        "iat": now_time,
        "data": data
    }
    return dic


class User(object):
    __instance__ = None
    __slots__ = ['uid', 'name', 'level', 'tid']

    def __new__(cls, *args, **kwargs):
        if not cls.__instance__:
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__

    def __init__(self, uid, name, level, tid):
        self.uid = uid
        self.name = name
        self.level = level
        self.tid = tid

    def to_dict(self):
        return {'uid': self.uid, 'name': self.name, 'level': self.level, 'tid': self.tid}


w_user = User(-1, -1, -1, -1)


def clean_user():
    with Lock():
        w_user.uid = -1
        w_user.name = -1
        w_user.level = -1
        w_user.tid = -1


def fill_user(data):
    with Lock():
        w_user.uid = data['uid']
        w_user.name = data['name']
        w_user.level = data['level']
        w_user.tid = data['tid']
