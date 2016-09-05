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

class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, id):
        self.inbox.push(id)

    def dequeue(self):
        if self.outbox.isEmpty:
            while (len(self.inbox.items) > 0):
                self.outbox.push(self.inbox.peek())
                self.inbox.pop()
        self.outbox.pop()


a = Queue()
a.enqueue(10)
a.enqueue(20)
a.enqueue(30)
a.enqueue(40)
print a.inbox.items
a.dequeue()
print a.outbox.items
a.dequeue()
print a.outbox.items
a.dequeue()
print a.outbox.items
