class Link:

    def __init__(self, id, next=None):
        self.id = id
        self.next = next

class LinkedList:
    def __init__(self, first=None):
        self.first = first

    def insert(self, id):
        new_node = Link(id)
        new_node.next = self.first
        self.first = new_node

    def display(self, head):
        while (head != None):
            print head.id
            head = head.next


def add_list(a, b):
    c = Link(0)
    move = c
    carry = 0
    while(a != None or b != None):
        sum = carry
        if a != None:
            sum += a.id
        if b != None:
            sum += b.id
        
        a = a.next
        b = b.next
        new_node = Link(sum%10)
        move.next = new_node
        move = move.next
        carry = sum/10
    if carry > 0:
        new_node = Link(carry)
        move.next = new_node
    
    return c.next

a = LinkedList()
a.insert(2)
a.insert(5)
a.insert(1)
b = LinkedList()
b.insert(2)
b.insert(5)
b.insert(9)
out = add_list(a.first, b.first)
while(out != None):
    print out.id
    out = out.next
