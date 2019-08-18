class Square:
    square_list = []

    def __init__(self, s):
        if s > 0:
            self.side = s
            self.square_list.append(self)
        else:
            raise ValueError

    def __repr__(self):
        return 'Square(side: {}, area: {})'.format(self.side, self.area())

    def __str__(self):
        return 'Square with side {} and area {}'.format(self.side, self.area())

    def area(self):
        return 4 * self.side


# square = Square(5)
# square2 = Square(6)
# print(Square.square_list)
# for sq in Square.square_list:
#     print(sq)
#     print(repr(sq))
