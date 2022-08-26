import time

from sanic import text, Blueprint

blue = Blueprint(__name__, url_prefix='/')


@blue.route('del', ["GET"])
async def sync_handler0(request):
    return text("I said foo! 111")


@blue.route('get', ["GET"])
async def sync_handler1(request):
    return text("I said foo! 222")


@blue.route('add', ["GET"])
async def sync_handler2(request):
    return text("I said foo! 333")
