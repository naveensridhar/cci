class Link:

	def __init__(self, id=None, next=None):
		self.id = id
		self.next = next


class LinkedList:

	def __init__(self, first=None):
		self.first = first

	def insert(self, id):
		new_node = Link(id)
		new_node.next = self.first
		self.first = new_node

	def display_list(self):
		current = self.first
		while current != None:
			print current.id
			current = current.next

	def find_middle_node(self):
		single_mover = self.first
		double_mover = self.first
		while double_mover != None:
			if double_mover.next == None:
				return single_mover.id
			single_mover = single_mover.next
			double_mover = double_mover.next.next
		return single_mover.id


test = LinkedList()
test.insert(10)
test.insert(20)
test.insert(30)
test.insert(40)
test.insert(40)
test.insert(40)
test.insert(50)
test.display_list()
print test.find_middle_node()


