# ESP32/ESP8266 Analog Readings with MicroPython:
# https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/

from machine import Pin, ADC
from time import sleep

DELAY_SEC = 1

pot = ADC(Pin(34))          # Configurar el pin 34 para ADC (entrada analógica)
pot.atten(ADC.ATTN_11DB)    # Configurar el rango de tensión:
                            #   - ADC.ATTN_0DB    : 0V a 1.2V (por defecto)
                            #   - ADC.ATTN_2_5DB  : 0V a 1.5V
                            #   - ADC.ATTN_6DB    : 0V a 2.0V
                            #   - ADC.ATTN_11DB   : 0V a 3.3V
pot.width(ADC.WIDTH_10BIT)  # Configurar la resolución:
                            #   - ADC.WIDTH_9BIT  : 0 a  511
                            #   - ADC.WIDTH_10BIT : 0 a 1023
                            #   - ADC.WIDTH_11BIT : 0 a 2047
                            #   - ADC.WIDTH_12BIT : 0 a 4095 (por defecto)

print("ATTN VALUES:")
print("  - ADC.ATTN_0DB    : ", ADC.ATTN_0DB)    # 0
print("  - ADC.ATTN_2_5DB  : ", ADC.ATTN_2_5DB)  # 1
print("  - ADC.ATTN_6DB    : ", ADC.ATTN_6DB)    # 2
print("  - ADC.ATTN_11DB   : ", ADC.ATTN_11DB)   # 3
print()
print("WIDTH VALUES:")
print("  - ADC.WIDTH_9BIT  :", ADC.WIDTH_9BIT)   #  9
print("  - ADC.WIDTH_10BIT :", ADC.WIDTH_10BIT)  # 10
print("  - ADC.WIDTH_11BIT :", ADC.WIDTH_11BIT)  # 11
print("  - ADC.WIDTH_12BIT :", ADC.WIDTH_12BIT)  # 12
print()

while True:
    pot_value = pot.read()    # Leer el valor del potenciometro
    print("%-10s: %7.2fV" % ("tension", 3.3 * (pot_value / 1023)))
    print("%-10s: %7.2f%%" % ("porcentaje", (pot_value * 100) / 1023))
    print("%-10s: %4d" % ("valor", pot_value))
    print()
    sleep(DELAY_SEC)
