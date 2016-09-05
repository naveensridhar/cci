class Stack:
    def __init__(self):
        self.items = []

    def push(self, id):
        self.items.append(id)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []



a = Stack()
a.push(10)
a.push(20)
print a.items
a.pop()
a.pop()
print a.items
