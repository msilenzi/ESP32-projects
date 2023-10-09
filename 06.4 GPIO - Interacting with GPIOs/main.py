# https://randomnerdtutorials.com/micropython-gpios-esp32-esp8266/

from machine import Pin, ADC, PWM
from time import sleep

DELAY_SEC = 0.1

led = Pin(2, Pin.OUT)
button = Pin(15, Pin.IN)

pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)  # Readings with 10 bit resolution (from 0 to 1023)
pot.atten(ADC.ATTN_11DB)    # Read voltage from 0 to 3.3 V.

led_pwm = PWM(Pin(4),5000)

while True:
    button_state = button.value()
    led.value(button_state)

    pot_value = pot.read()
    led_pwm.duty(pot_value)

    sleep(DELAY_SEC)
