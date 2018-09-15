import math


class Vector:

    def __init__(self, x, y, z):
        self.y = y
        self.z = z
        self.x = x


    def __add__(self, other):
        a = self.x + other.x
        b = self.y + other.y
        c = self.z + other.z
        return Vector(a, b, c)


    def __len__(self):
        return int(math.sqrt((self.x**2.0) + (self.y**2.0) + (self.z**2.0)))

    def __str__(self):
        return f'Vector[{self.x}, {self.y}, {self.z}]'