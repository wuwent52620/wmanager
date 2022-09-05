#!/usr/bin/env python

"""
FileName: my_middleware
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 20:09:04
"""
import jwt

from auth import clean_user, fill_user


async def init_user(request):
    """ 实现请求的前期处理，比如验证签名 """
    if request.path != "/api/auth/login":
        token = request.headers.get('token')
        if token:
            try:
                token_data = jwt.decode(token, request.app.config.SECRET, algorithms=["HS256"])
            except jwt.exceptions.InvalidTokenError:
                clean_user()
                return False
            else:
                fill_user(token_data["data"])
        else:
            clean_user()


async def print_on_response(request, response):
    """ 实现响应的后续处理 """
    print("I print when a response is returned by the server")
