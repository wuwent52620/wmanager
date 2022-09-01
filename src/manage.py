from contextvars import ContextVar

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from middlewares.my_middleware import print_on_request, print_on_response
from src import app

from models import system, user

bind = create_async_engine(app.config.SQLALCHEMY_DATABASE_AIO)
_base_model_session_ctx = ContextVar("session")

app.register_middleware(print_on_request, attach_to='request')
app.register_middleware(print_on_response, attach_to='response')


@app.middleware("request")
async def inject_session(request):
    request.ctx.session = sessionmaker(bind, AsyncSession, expire_on_commit=False)()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


@app.middleware("response")
async def close_session(request, response):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()


from views import api

app.blueprint(api)

# 启动服务
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True, workers=4)
