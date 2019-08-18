class Stack:
    def __init__(self):
        self.i = 0
        self.items = []

    def __iter__(self):
        return self

    def __next__(self):
        index = self.i
        self.i += 1
        if self.i > len(self.items):
            raise StopIteration
        return index

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        return self.items

    def pop(self):
        if not self.is_empty():
            return self.items.pop(len(self.items)-1)
        raise IndexError('pop from empty list')

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


def main():
    stack1 = Stack()
    for i in range(0, 6):
        stack1.push(i)

    try:
        for i in range(0, 7):
            print(stack1.pop())
    except IndexError as error:
        print('Error: {}'.format(error))


if __name__ is "__main__" or "ch21-1stack":
    main()
