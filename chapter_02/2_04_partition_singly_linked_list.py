# Create two link and move the lesser no. to the left link adn greater one to th eright link
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
#1
#4
#3
#2
#5
#2
    def partition_linked_list(self, value):
        front = Link(0)
        front_head = front
        back = Link(0)
        back_head = back

        head = self.first
        while (head != None):
            if head.id >= value:
                back.next = head
                back = back.next
            else: 
                front.next = head
                front = front.next
            head = head.next
        front.next = back_head.next
        back.next = None
        return front_head.next


l = LinkedList()
l.insert(2)
l.insert(5)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(1)
print "---------Input------------"
l.display(l.first)
a = l.partition_linked_list(3)
print "---------Output------------"
l.display(a)
