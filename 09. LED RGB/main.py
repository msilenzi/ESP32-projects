from time import sleep
from LedRGB import LedRGB

led = LedRGB(5, 18, 19, LedRGB.COMMON_ANODE)

while True:
    led.turn_on_red()
    sleep(1)
    led.turn_on_green()
    sleep(1)
    led.turn_on_blue()
    sleep(1)
