from machine import Pin, PWM

MAX_DUTY = 1023


def color_to_duty(color_value: int) -> int:
    return (color_value * MAX_DUTY) // 255


class PinRGB:
    def __init__(self, pin_number: int, is_common_anode: bool):
        self._pin = PWM(Pin(pin_number, Pin.OUT), duty=0)
        self._is_common_anode = is_common_anode
        self._value = 0
    
    def set_color(self, color: int):
        self._value = color
        duty = color_to_duty(color)
        self._pin.duty(duty if self._is_common_anode else MAX_DUTY - duty)
    
    def get_color(self) -> int:
        return self._value