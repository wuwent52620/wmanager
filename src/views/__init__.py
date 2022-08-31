from sanic import Blueprint
from .user import user
from .system import system
from .auth import auth

api = Blueprint.group(user, system, auth, url_prefix="/api")
