# Have to pointers. One slow pointer and another fast pointer. Move slow pointer at 1 step at a time. Move fast pointer at 2 steps at a time. If it is circula#r, they will meet at some point for sure. They meet at a place from where it is k steps to the start of the loop. Now move one pointer to the beginning of th#e  linked list. Move both the pointers at 1 step at a time

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

    def insert_back(self, node_number):
        head = self.first
        count = 0
        while(head != None):
            count = count + 1
            if count == node_number:
                old_node = head
            if head.next == None:
                head.next = old_node
                break
            head = head.next

    def collision_node(self):
        slow_runner = self.first
        fast_runner = self.first
        while(fast_runner != None and fast_runner.next != None):
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
            if slow_runner == fast_runner:
                return slow_runner
        return False

    def find_beginning_node(self, collision_node):
        slow_runner = self.first
        while (slow_runner != collision_node):
            slow_runner = slow_runner.next
            collision_node = collision_node.next
        return slow_runner

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
a.insert_back(5)
collision = a.collision_node()
if collision:
    print a.find_beginning_node(collision).id

