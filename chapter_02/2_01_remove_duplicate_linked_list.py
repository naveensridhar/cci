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
        current = self.first
        while(current != None):
            runner = current
            while(runner.next != None):
                if runner.next.id == current.id:
                    runner.next = runner.next.next
                else:
                    runner = runner.next

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
new.removeDuplicatesWithoutBuffer()
print "----------------"
new.displayList()
