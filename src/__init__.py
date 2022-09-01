import sanic
from sanic import Sanic, Blueprint
from config import config
from exception import BadRequest, Unauthorized, Forbidden, NotFound, RequestTimeout, ServerError
from utils.exceptions import CustomHandler
app = Sanic("WManagerApp")
app.update_config(config['default'])  # 通过此处的更换就可以实现切换环境
app.config.SECRET = "W_MANAGER_WWT"
app.error_handler = CustomHandler()


class MyBlueprint(Blueprint):
    def __init__(self, name=None, url_prefix=None, host=None, version=None, strict_slashes=None, version_prefix="/v"):
        name = name.replace(".", "")
        super().__init__(name, url_prefix, host, version, strict_slashes, version_prefix)


sanic.Blueprint = MyBlueprint

all_json_errors = [BadRequest, Unauthorized, Forbidden,
                   NotFound, RequestTimeout, ServerError]
