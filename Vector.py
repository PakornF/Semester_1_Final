import math

class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Vector(x={self.x}, y={self.y})'

    def dot(self, v):
        return (self.x * v.x) + (self.y * v.y)

    def add(self, v):
        ax = self.x + v.x
        ay = self.y + v.y
        return Vector(ax, ay)

    def subtract(self, v):
        return Vector((self.x - v.x), (self.y - v.y))

    def multiply(self, s):
        return Vector((self.x * s), (self.y * s))

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        return Vector(self.x * scale, self.y * scale)

    def __rmul__(self, scale):
        return self.__mul__(scale)