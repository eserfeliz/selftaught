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

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        return self.items

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


def main():
    stack1 = Stack()
    # print(stack1.is_empty())  # True
    # stack1.push(1)
    # print(stack1.is_empty())  # False
    # print(stack1.pop())       # 1
    # print(stack1.is_empty())  # True
    for i in range(0, 6):
        stack1.push(i)
    # print(stack1.peek())      # 5        Item atop the stack
    # print(stack1.size())      # 6        [0, 1, 2, 3, 4, 5]
    # print(len(stack1))
    # print(dir(stack1))
    # for item in stack1:
    #     print(str(item))
    # print(str(stack1))


if __name__ is "__main__" or "ch21-1stack":
    main()
