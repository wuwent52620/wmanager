from sanic import html

from middlewares.my_middleware import print_on_request, print_on_response
from src import app

app.register_middleware(print_on_request, attach_to='request')
app.register_middleware(print_on_response, attach_to='response')


# 注册各个模块

# 混合添加单个函数
async def hello(request):
    return html("<h1>Hello</h1>")


app.add_route(hello, "/demo/hello", methods=['GET'])

# 启动服务
app.run(host="0.0.0.0", port=8000, debug=True)
