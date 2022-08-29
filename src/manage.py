from sanic import html

from middlewares.my_middleware import print_on_request, print_on_response
from src import app
from models import system, user
app.register_middleware(print_on_request, attach_to='request')
app.register_middleware(print_on_response, attach_to='response')
# app.register_middleware(inject_session, attach_to='response')
# app.register_middleware(close_session, attach_to='response')

from views import api

app.blueprint(api)


async def hello(request):
    return html("<h1>Hello</h1>")


app.add_route(hello, "/demo/hello", methods=['GET'])

# 启动服务
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9999, debug=True)
