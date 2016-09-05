
class Link:
    def __init__(self, id, next=None):
        self.id = id
        self.next = next

class LinkedList:
    def __init__(self, first=None):
        self.first=first

    def insert(self, id):
        new_node = Link(id)
        new_node.next = self.first
        self.first = new_node

    def reverse(self):
        prev = None
        current = self.first
        while(current != None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.first = prev


    def display(self):
        head = self.first
        while(head != None):
            print head.id
            head = head.next

a = LinkedList()
a.insert(100)
a.insert(90)
a.insert(80)
a.insert(70)
a.insert(60)
a.insert(50)
a.insert(40)
a.insert(30)
a.insert(20)
a.insert(10)
a.display()
a.reverse()
a.display()
