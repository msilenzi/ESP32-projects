from microdot_asyncio import Microdot, Response, send_file
from counter import Counter

# Server
app = Microdot()
Response.default_content_type = "text/html"

# Counters
counters = (Counter(), Counter())


def get_counters():
    dict_counters = []
    for i, counter in enumerate(counters):
        dict_counters.append({"id": i, "value": counter.get_value()})

    # for i in range(len(counters)):
    #     json_counters.append({'id': i, 'value': counters[i].get_value()})

    return dict_counters


# API


@app.get("/counters")
async def get_all_counters(request):
    return get_counters()


@app.post("/counters/<int:id>/increment")
async def increment_counter(request, id):
    if 0 <= id < len(counters):
        counters[id].increment()
        return get_counters()
    else:
        return {"error": "Invalid counter ID"}, 404


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
