from led_rgb import LedRGB
from time import sleep_ms

DELAY_MS = 1

led = LedRGB(5, 18, 19, True)
    
while True:
    # From red to green
    for i in range(LedRGB.MAX_DUTY + 1):
        led.set_red(LedRGB.MAX_DUTY - i)
        led.set_green(i)
        sleep_ms(DELAY_MS)
    
    # From green to blue
    for i in range(LedRGB.MAX_DUTY + 1):
        led.set_green(LedRGB.MAX_DUTY - i)
        led.set_blue(i)
        sleep_ms(DELAY_MS)
    
    # From blue to red
    for i in range(LedRGB.MAX_DUTY + 1):
        led.set_blue(LedRGB.MAX_DUTY - i)
        led.set_red(i)
        sleep_ms(DELAY_MS)
