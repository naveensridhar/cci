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
     
        head = self.first
        while(head != None):
            print head.id
            head = head.next

    def length(self):
        head = self.first
        count = 0
        while(head != None):
            count += 1
            head = head.next
        return count

    def shift_index(self, k):
        l = self.length()
        shift = l-k
       
        head = self.first
        current = head
        count = 0
        while(current.next != None):
            count += 1
            if (count == shift):
                new_last = current
            current = current.next
        nextone = new_last.next
        new_last.next = None
        current.next = self.first
        self.first = nextone
            

        
        
new = LinkedList()
new.insert(40)
new.insert(30)
new.insert(20)
new.insert(10)
new.insert(15)
new.insert(75)
new.displayList()
print "----------------------"
new.shift_index(2)
new.displayList()

