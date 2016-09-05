class Stack:
    def __init__(self):
        self.item = []
        self.length = 0

    def push(self, id):
        self.item.append(id)
        self.length += 1

    def pop(self):
        self.item.pop()
        self.length -= 1

    def peek(self):
        return self.item[self.length - 1]

    
class SetOfStacks:
    def __init__(self, max_length):
        self.setstack = []
        self.max_length = max_length

    def push1(self, id):
        if self.setstack == [] or self.setstack[len(self.setstack) - 1].length >= self.max_length:
            new_stack = Stack()
            self.setstack.append(new_stack)
        self.setstack[len(self.setstack) - 1].push(id)

    def pop1(self):
        self.setstack[len(self.setstack) - 1].pop()
        if self.setstack[len(self.setstack) - 1].length == 0:
            self.setstack.pop()


    def popAt(self, index):
        if index < len(self.setstack) - 1:
            self.setstack[index].pop()
        if self.setstack[index].length == 0:
            del self.setstack[index]

a = SetOfStacks(5)
a.push1(10)
a.push1(10)
a.push1(10)
a.push1(10)
a.push1(10)
print a.setstack[0].item
a.push1(20)
print a.setstack[1].item
a.pop1()
print len(a.setstack)
a.push1(20)
a.push1(20)
a.push1(20)
a.push1(20)
a.push1(20)
print a.setstack[1].item
a.popAt(0)
a.popAt(0)
a.popAt(0)
a.popAt(0)
a.popAt(0)
print a.setstack[0].item
