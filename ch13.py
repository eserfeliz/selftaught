class Shape:
    def what_am_i(self):
        if self:
            print('I am a shape')


class Rectangle(Shape):
    def __init__(self, l, w):
        if l > 0 and w > 0:
            self.length = l
            self.width = w
        else:
            raise ValueError

    def calculate_perimeter(self):
        return (2 * self.length) + (2 * self.width)


class Square(Shape):
    def __init__(self, s):
        if s > 0:
            self.side = s
        else:
            raise ValueError

    def calculate_perimeter(self):
        return 4 * self.side

    def change_size(self, delta):
        self.side += delta


class Rider:
    def __init__(self, n):
        self.name = n


class Horse:
    def __init__(self, n, r):
        self.name = n
        self.rider = r


# square = Square(4)
# rect = Rectangle(4, 5)
#
# print(square.calculate_perimeter())
# print(rect.calculate_perimeter())

# try:
#     square = Square(0)
#     print(square.calculate_perimeter())
#     square.change_size(-1)
#     print(square.calculate_perimeter())
# except ValueError:
#     print("Error: the side of a square must be greater than 0.")

# try:
#     rect = Rectangle(-1, 4)
#     print(rect.calculate_perimeter())
# except ValueError:
#     print("Error: the length and the width of a rectangle must both be greater than 0.")
# square = Square(5)
# rect = Rectangle(5, 4)
# square.what_am_i()
# rect.what_am_i()

# chuck = Rider('Chuck Norris')
# betsy = Horse('Betsy', chuck)
#
# print(betsy.rider.name)