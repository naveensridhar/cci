class Link:
	# Current
	def __init__(self, id=None, next=None):
		self.id = id
		self.next = next

	def displayLink(self):
		return self.id

class LinkedList:

	def __init__(self, first=None):
		self.first = None

	def insert(self, id):
		new_link = Link(id)
		new_link.next = self.first
		self.first = new_link

	def displayLinked(self):
		current = self.first
		while (current != None):
			print current.id, "Hi"
			current = current.next

	def isEmpty(self):
		return self.first == None

	def reverse(self):
		current = self.first
		prev = None
		i = 0
		while current != None:
			tmp = current.next
			current.next = prev
			prev = current
			current = tmp
		self.first = prev

test = LinkedList()

test.insert(10)
test.insert(20)
test.insert(30)
test.insert(40)

test.displayLinked()
test.reverse()
test.displayLinked()


