from pin_rgb import PinRGB

class LedRGB:
    def __init__(self, pin_r: int, pin_g: int, pin_b: int, is_common_anode: bool):
        self._red = PinRGB(pin_r, is_common_anode)
        self._green = PinRGB(pin_g, is_common_anode)
        self._blue = PinRGB(pin_b, is_common_anode)
        self.turn_off()

    def set_red(self, color: int):
        self._red.set_color(color)

    def set_green(self, color: int):
        self._green.set_color(color)

    def set_blue(self, color: int):
        self._blue.set_color(color)

    def set_rgb(self, r_color: int, g_color: int, b_color: int):
        self.set_red(r_color)
        self.set_green(g_color)
        self.set_blue(b_color)

    def turn_off(self):
        self.set_rgb(0, 0, 0)

    def get_rgb(self):
        return {
            "red": self._red.get_color(),
            "green": self._green.get_color(),
            "blue": self._blue.get_color(),
        }
