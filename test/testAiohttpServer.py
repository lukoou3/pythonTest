#coding=utf-8
from aiohttp import web
from aiohttp.web_request import Request

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

@routes.get('/status')
async def hello(request):
    return web.json_response({'error': 'Todo not found'}, status=404)

@routes.get('/json')
async def get_all_todos(request):
    TODOS = [{'name':"aa"},{'name':"bb"}]
    return web.json_response([
        {'id': idx, **todo} for idx, todo in enumerate(TODOS)
    ])

@routes.get(r'/name/{name}')
async def variable_handler(request):
    return web.Response(text="Hello, {}".format(request.match_info['name']))

@routes.get(r'/name/{name}/{num:\d+}')
async def rvariable_handler(request):
    return web.Response(text="Hello, {},{}".format(request.match_info['name'],request.match_info['num']))

@routes.get('/get')
async def gte(request):
    data = request.query
    return web.Response(text="Hello, {}".format(data.get('name')))

@routes.post('/post')
async def handler(request):
    data = await request.post()
    return web.Response(text="Hello, {}".format(data.get('name')))

app = web.Application()
routes.static('/py', "./",show_index=True)
app.add_routes(routes)
#app.router.add_static('/py', "./",show_index=True)
#app.add_routes([web.get('/', hello)])

web.run_app(app,port=8081)
