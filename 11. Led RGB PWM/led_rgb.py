from machine import Pin, PWM

class LedRGB:
    MAX_DUTY = 1023
    
    def __init__(self, pin_r: int, pin_g: int, pin_b: int, is_common_anode: bool):
        self._red = PWM(Pin(pin_r), 5000)
        self._green = PWM(Pin(pin_g), 5000)
        self._blue = PWM(Pin(pin_b), 5000)
        self._is_common_anode = is_common_anode
        self._off_duty = 0 if is_common_anode else LedRGB.MAX_DUTY
        self.turn_off()
    
    def turn_off(self):
        self._red.duty(self._off_duty)
        self._green.duty(self._off_duty)
        self._blue.duty(self._off_duty)
    
    def _set_color(self, pin: Pin, duty: int):
        pin.duty(duty if self._is_common_anode else LedRGB.MAX_DUTY - duty)
    
    def set_red(self, duty: int):
        self._set_color(self._red, duty)
    
    def set_green(self, duty: int):
        self._set_color(self._green, duty)
    
    def set_blue(self, duty: int):
        self._set_color(self._blue, duty)
    
    def set_rgb(self, r_duty: int, g_duty: int, b_duty: int):
        self._set_color(self._red, r_duty)
        self._set_color(self._green, g_duty)
        self._set_color(self._blue, b_duty)
