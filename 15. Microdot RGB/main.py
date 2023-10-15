from microdot_asyncio import Microdot, Response, send_file
from led_rgb import LedRGB


def is_valid_color(color: int) -> bool:
    return 0 <= color <= 255


def is_valid_rgb(rgb_color: dict) -> bool:
    return (
        is_valid_color(rgb_color["red"])
        and is_valid_color(rgb_color["green"])
        and is_valid_color(rgb_color["blue"])
    )


# Server
app = Microdot()
Response.default_content_type = "text/html"

led = LedRGB(5, 18, 19, True)


# API


@app.get("/led_rgb")
async def get_rbg_values(request):
    return led.get_rgb()


@app.post("/led_rgb")
async def set_rgb_red(request):
    rgb_color = request.json
    if is_valid_rgb(rgb_color):
        led.set_rgb(rgb_color["red"], rgb_color["green"], rgb_color["blue"])
        return led.get_rgb()
    else:
        return {"error": "Invalid rgb color"}, 400


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


app.run()
