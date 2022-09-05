import os

from sanic import json


def json_response(state_code=200, **kwargs):
    return json(body=kwargs, status=state_code)


BaseDir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
