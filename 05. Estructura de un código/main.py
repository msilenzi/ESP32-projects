import time     # Permite acceder a funciones de tiempo como sleep
import machine  # Permite acceder al hardware del ESP32 para poder configurarlo
                # y manipularlo.
            
TIEMPO_MS = 500


# Configurar pines GPIO del ESP32 como E/S

pin_boton = machine.Pin(1, machine.Pin.IN)   # Configurar pin 1 como entrada
pin_led   = machine.Pin(2, machine.Pin.OUT)  # Configurar pin 2 como salida


# Código

""" Hacer que un LED se encienda al presionar un botón, si el botón no está
    presionado el LED se apaga"""

while True:  # Simulamos el loop() de Arduino
    led.value(boton.value())
    time.sleep_ms(TIEMPO_MS)
