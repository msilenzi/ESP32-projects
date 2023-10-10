from machine import Pin
from microdot_asyncio import Microdot, Response, send_file


# Server
app = Microdot()
Response.default_content_type = "text/html"

# Leds
leds = tuple(Pin(p, Pin.OUT, value=0) for p in [4, 16, 2])
# leds = (Pin(4, Pin.OUT, value=0), Pin(16, Pin.OUT, value=0), Pin(2, Pin.OUT, value=0))


def get_leds_values():
    """returns a list of the LEDs values"""
    return list(map(lambda led: led.value(), leds))


# API


@app.get("/leds")
async def get_all_leds_values(request):
    return get_leds_values()


@app.post("/leds/<int:id>/off")
async def turn_off_led(request, id):
    if 0 <= id < len(leds):
        leds[id].off()
        return Response(status_code=204)
    else:
        return {"error": "Invalid LED ID"}, 404


@app.post("/leds/<int:id>/on")
async def turn_on_led(request, id):
    if 0 <= id < len(leds):
        leds[id].on()
        return Response(status_code=204)
    else:
        return {"error": "Invalid LED ID"}, 404


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
