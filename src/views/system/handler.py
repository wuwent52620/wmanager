import time

from sanic import text, Blueprint

blue = Blueprint(__name__, url_prefix='/')


@blue.get('del')
async def sync_handler0(request):
    return text("I said foo! 111")


@blue.get('get')
async def sync_handler1(request):
    return text("I said foo! 222")


@blue.get('add')
async def sync_handler2(request):
    return text("I said foo! 333")
