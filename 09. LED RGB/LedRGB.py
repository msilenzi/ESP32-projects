from machine import Pin

class LedRGB:
    COMMON_ANODE = 1
    COMMON_CATHODE = 0
    
    def __init__(self, pin_r: int, pin_g: int, pin_b: int, common):
        self._red = Pin(pin_r, Pin.OUT)
        self._green = Pin(pin_g, Pin.OUT)
        self._blue = Pin(pin_b, Pin.OUT)
        self._on_value = common
        self.turn_off()
    
    def turn_off(self):
        self._red.value(not self._on_value)
        self._green.value(not self._on_value)
        self._blue.value(not self._on_value)
    
    def turn_on_red(self):
        self._red.value(self._on_value)
        self._green.value(not self._on_value)
        self._blue.value(not self._on_value)
    
    def turn_on_green(self):
        self._red.value(not self._on_value)
        self._green.value(self._on_value)
        self._blue.value(not self._on_value)
        
    def turn_on_blue(self):
        self._red.value(not self._on_value)
        self._green.value(not self._on_value)
        self._blue.value(self._on_value)
