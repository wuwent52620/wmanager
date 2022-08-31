from sanic.exceptions import SanicException
from sanic.handlers import ErrorHandler


class CustomHandler(ErrorHandler):

    def default(self, request, exception):
        if not isinstance(exception, SanicException):
            print(exception)
        return super().default(request, exception)


class ResponseError(Exception):
    def __init__(self, *args):
        self.data = args[0]
        self.code = args[1]
        super().__init__(*args)
