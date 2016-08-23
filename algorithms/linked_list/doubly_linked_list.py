class Link:

	def __init__(self, id, next=None, prev=None):
		self.id = id
		self.next = None
		self.prev = None

class DoubleList:

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def append(self, id):
		new_link = Link(id)
		if self.head == None:
			self.head = new_link
			self.tail = new_link
		else:
			new_link.prev = self.tail
			self.tail.next = new_link
			self.tail = new_link

	def show(self):
		current = self.head
		while(current != None):
			print current.id
			current = current.next

	def remove(self, id):
		current = self.head
		while(current!=None):
			if id == current.id:
				if current.prev != None:
					if current.next != None:
						current.prev.next = current.next
						current.next.prev = current.prev
					else:
						current.prev.next = None
				else:
					current.next.prev = None
			current = current.next



d = DoubleList()
 
d.append(5)
d.append(6)
d.append(50)
d.append(30)
d.remove(50)
d.show()



