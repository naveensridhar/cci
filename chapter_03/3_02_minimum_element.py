class Stack:
    def __init__(self):
        self.items = []
        self.mini = []

    def push(self, id):
        if self.isEmpty():
            self.mini.append(id)
        else:
            peek = self.mini[len(self.items) - 1]
            if peek < id:
                self.mini.append(peek)
            else:
                self.mini.append(id) 
        self.items.append(id)

    def pop(self):
        self.mini.pop()
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self, list):
        return list[len(self.items) - 1]

a = Stack()
a.push(10)
a.push(20)
a.push(11)
a.push(10)
a.push(21)
print a.peek(a.items)
print a.peek(a.mini)
