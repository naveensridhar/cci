class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, id):
        self.length += 1
        self.items.append(id)

    def pop(self):
        self.length -= 1
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[self.length -1]


def sort_ascending(a):
    output_stack = Stack()
    
