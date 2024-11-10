import math

class Vector(object):
    def __init__(self, x=0, y=0):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, value):
        self._x = float(value)

    @y.setter
    def y(self, value):
        self._y = float(value)

    def __add__(self, other):
        c = self
        c += other
        return c

    def __sub__(self, other):
        c = self
        c -= other
        return c

    def __iadd__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.x + other.x, self.y + other.y)

    def __isub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return not (self == other)

    def length(self):
        return math.hypot(self.x, self.y)

    def __str__(self):
        return f'({self.x}, {self.y})'

a = Vector(5, 7.8)
b = Vector(13.9, 25.3)

c = a + b

print(c)
