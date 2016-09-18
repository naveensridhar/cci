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

    def check_palindrome(self):
        slow_runner = self.first
        fast_runner = self.first
        
        stack = []
       
        while(fast_runner != None and fast_runner.next != None):
            stack.append(slow_runner.id)
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
        
        if fast_runner != None:
            slow_runner = slow_runner.next

        while( slow_runner != None):
            if slow_runner.id != stack.pop():
                return False
            slow_runner = slow_runner.next

        return True

        
    def display(self):
        head = self.first
        while(head != None):
            print head.id
            head = head.next


a = LinkedList()
a.insert("a")
a.insert("d")
a.insert("a")
a.insert("a")
a.insert("d")
a.insert("a")
a.insert("a")

a.display()


print a.check_palindrome()
