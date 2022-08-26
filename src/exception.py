class BadRequest(Exception):
    pass


class Unauthorized(Exception):
    pass


class Forbidden(Exception):
    pass


class NotFound(Exception):
    pass


class RequestTimeout(Exception):
    pass


class ServerError(Exception):
    pass
