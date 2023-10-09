from microdot_asyncio import Microdot, Response, send_file

app = Microdot()
Response.default_content_type = 'text/html'


@app.route('/')
async def index(request):
    return send_file('static/index.html')


@app.route('/static/<path:path>')
def static (request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)

app.run(debug=True)
