class Link:
    def __init__(self, id, next=None):
        self.id = id
        self.next = next


class LinkedList:
    def __init__(self, first=None):
        self.first = first

    def insert(self, id):
        new_link = Link(id)
        new_link.next = self.first
        self.first = new_link

    def display(self):
        current = self.first
        while(current != None):
            print current.id
            current = current.next

    def remove_node(self,current):
        if current.next != None:
            next_node = current.next
            current.id = next_node.id
            current.next = next_node.next
            next_node = None
            return True
        else:
            return False
l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.display()
a = l.remove_node(l.first.next.next.next)
l.display()
