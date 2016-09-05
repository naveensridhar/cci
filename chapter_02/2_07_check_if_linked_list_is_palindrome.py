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
        
        while(fast_runner != None and fast_runner.next != None):
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next

        second_head = slow_runner
        slow_runner = None

        prev = second_head
        current = prev.next

        while(current != None and current.next != None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        test = second_head
        while (test != None):
            print test.id
            test = test.next

        
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
a.display()


a.check_palindrome()
