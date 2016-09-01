# Remove duplicated from linked list
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
        
    def delete(self, id):
        link = self.first
        prev = link
        while(link.id != id):
            if link.next == None:
                return None
            else:
                prev = link
                link = link.next
        if link == self.first:
            first = first.next
        else:
            prev.next = link.next
          
    def displayList(self):
     
        link = self.first
        while(link != None):
            print link.id
            link = link.next

    def removeDuplicatesWithBuffer(self):
        current = self.first
        dict = {}
        prev = current
        while(current != None):
            if current.id not in dict:
                dict[current.id] = 1
                prev = current
            else:
                prev.next = current.next
            current = current.next
                 
    def removeDuplicatesWithoutBuffer(self):
        # Not working
        current = self.first
        check = current
        prev = current
        
        while(current != None and current.next != None):
            check = current.next
            prev = current
            while(check != None):
                if current.id == check.id:
                    print "test"
                    prev.next = check.next
                prev = check
                check = check.next
            current = current.next
 
new = LinkedList()
new.insert(30)
new.insert(30)
new.insert(30)
new.insert(30)
new.insert(30)
print "----------------"
new.displayList() 
new.delete(20)
print "----------------"
new.displayList()
new.removeDuplicatesWithBuffer()
print "----------------"
new.displayList()
