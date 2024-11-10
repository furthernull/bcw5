import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self==other)

    def distance(self, other):
        return math.hypot(self.x-other.x, self.y-other.y)

a = Point(0, 3)
b = Point(4, 0)

print(a.distance(b))