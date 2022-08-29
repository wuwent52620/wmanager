#!/usr/bin/env python

"""
FileName: my_middleware
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 20:09:04
"""

from contextvars import ContextVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


async def print_on_request(request):
    """ 实现请求的前期处理，比如验证签名 """
    print("I print when a request is received by the server")


async def print_on_response(request, response):
    """ 实现响应的后续处理 """
    print("I print when a response is returned by the server")


_base_model_session_ctx = ContextVar("session")


# async def inject_session(request):
#     from base import bind
#     request.ctx.session = sessionmaker(bind, AsyncSession, expire_on_commit=False)()
#     request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)
#
#
# async def close_session(request, response):
#     if hasattr(request.ctx, "session_ctx_token"):
#         _base_model_session_ctx.reset(request.ctx.session_ctx_token)
#         await request.ctx.session.close()
