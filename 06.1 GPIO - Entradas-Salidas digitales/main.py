# https://randomnerdtutorials.com/esp32-esp8266-digital-inputs-digital-outputs-micropython/

from machine import Pin, ADC, PWM
from time import sleep

DELAY_SEC = 0.1

led = Pin(2, Pin.OUT)
button = Pin(15, Pin.IN)

while True:
    button_state = button.value()
    led.value(button_state)

    sleep(DELAY_SEC)
