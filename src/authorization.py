from functools import wraps

from sanic import text

from auth import w_user


def level_required(level):
    """ token校验装饰器 """

    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            user = w_user

            if user.level >= level:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return text("抱歉，你没有此操作权限", 401)

        return decorated_function

    return decorator
