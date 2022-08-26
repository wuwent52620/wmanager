from sanic import Blueprint
from .user import user
from .system import system

api = Blueprint.group(user, system, url_prefix="/api")
