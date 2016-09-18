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
        
    def insert_overlap(self, new_link, old_link, index):
        while(new_link.next != None):
            new_link = new_link.next

        
        count = 1
        while(old_link != None):
            if index == count:
                new_link.next = old_link
                break
            count += 1
            old_link = old_link.next 

    def length(self):
        head = self.first
        count = 0
        while(head != None):
            count += 1
            head = head.next
        return count



def is_overlapping(l1, l2):
    len1 = l1.length()
    len2 = l2.length()
    head1 = l1.first
    head2 = l2.first
    if len1 > len2:
        forward = len1-len2
        while (forward > 0):
            head1 = head1.next
            forward -= 1
    else:
        forward = len2-len1
        while (forward > 0):
            head2 = head2.next
            forward -= 1
    while(head1 != None and head2 != None and head1 != head2):
        head1 = head1.next
        head2 = head2.next
    return head1
         
new = LinkedList()
new.insert(40)
new.insert(30)
new.insert(20)
new.insert(10)
new.insert(60)
new.insert(70)
new.displayList()
print new.length()
print "----------------"
one_more = LinkedList()
one_more.insert(35)
one_more.insert(25)
one_more.insert(15)
one_more.insert(45)
one_more.insert_overlap(one_more.first, new.first, 2)
one_more.displayList()
print one_more.length()
val = is_overlapping(new, one_more)
if val != None:
    print val.id 


