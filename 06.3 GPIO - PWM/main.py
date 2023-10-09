"""
    En el ESP32 podemos habilitar el PWM en cualquier pin que se pueda utilizar
    como salida.
"""

from machine import Pin, ADC, PWM
from time import sleep

DELAY_SEC = 0.05

pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)

led_pwm = PWM(Pin(4), 5000)

while True:
    pot_value = pot.read()
    led_pwm.duty(pot_value)
    print(pot_value)
    sleep(DELAY_SEC)
    
"""
    Si queremos imprimir múltiples valores en el plotter tenemos que usar una
    tupla: print((pot_value1, pot_value2, pot_value3))
"""
