class Link:
    def __init__(self, id, next=None):
        self.id = id
        self.next = next

    def display():
        return self.id 

class LinkedList:
          
    def __init__(self, first=None):
        self.first = None

    def insert(self, id):
        new_link = Link(id)
        new_link.next = self.first
        self.first = new_link

    def displayList(self):
     
        link = self.first
        while(link != None):
            print link.id
            link = link.next
        
def merge(l1, l2):
    merged = Link(0)
    current = merged
    while(l1!= None and l2!= None):
        if l1.id <= l2.id:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 if l2 is None else l1
    return merged.next 
        



new = LinkedList()
new.insert(40)
new.insert(30)
new.insert(20)
new.insert(10)
print "----------------"
one_more = LinkedList()
one_more.insert(35)
one_more.insert(25)
one_more.insert(15)
a = merge(new.first, one_more.first)
while a != None:
    print a.id
    a = a.next
