class Link:
    def __init__(self, id, next=None):
        self.id = id
        self.next = next

    def display():
        return self.id 

class LinkedList:
          
    def __init__(self, first=None):
        self.first = first

    def insert(self, id):
        new_link = Link(id)
        new_link.next = self.first
        self.first = new_link
    
    def displayList(self):
     
        link = self.first
        while(link != None):
            print link.id
            link = link.next

    def nth_kth(self, head, k):
        if head.next == None:
            return 0
        
        n = self.nth_kth(head.next, k) + 1
        if n == k:
            print head.id
        return n
        
linked_list = LinkedList()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)
linked_list.insert(50)
linked_list.nth_kth(linked_list.first, 2)
