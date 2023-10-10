from machine import Pin
from wifi_manager import WifiManager
from time import sleep

led = Pin(2, Pin.OUT, value=0)

for _ in range(6):
    led.value(not led.value())
    sleep(0.1)

wm = WifiManager()
wm.connect()

led.value(1)
