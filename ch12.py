class Apple:
    def __init__(self, n, c, o, g):
        """
        name refers to the object's cultivar
        group refers to the object's pollination group
        """

        self.name = n
        self.color = c
        self.origin = o
        self.group = g


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        import math as m

        return m.pi * m.pow(self.radius, 2)


# circle = Circle(3)
# print(circle.area())

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height) // 2


# triangle = Triangle(5, 10)
# print(triangle.area())

class Hexagon:
    def __init__(self, l):
        self.length_of_side = l

    def calculate_perimeter(self):
        return 6 * self.length_of_side


# hexagon = Hexagon(5)
# print(hexagon.calculate_perimeter())
