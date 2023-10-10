from microdot_asyncio import Microdot, Response, send_file
from counter import Counter

# Server
app = Microdot()
Response.default_content_type = "text/html"


# API


# Api go brrr...


# Static files


@app.route("/")
async def index(request):
    return send_file("static/index.html")


@app.route("/static/<path:path>")
async def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return send_file("static/" + path)


app.run(debug=True)
