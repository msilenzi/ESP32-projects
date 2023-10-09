class Counter:
    def __init__(self, initial_value=0):
        self._value = initial_value
    
    def increment(self):
        self._value += 1
        return self._value
    
    def get_value(self):
        return self._value
