class Link:
	
	def __init__(self, id=None, next=None):
		self.id = id
		self.next = next

class LinkedList:

	def __init__(self, first=None):
		self.first = first

	def insert(self, id):
		newLink = Link()
		newLink.id = id

		if self.first == None:
			self.first = newLink
		else:
			self.first, newLink.next = newLink, self.first

	def display_link(self):
		current = self.first
		while current != None:
			print current.id
			current = current.next

class Node:

	def __init__(self, id=None, lc=None, rc=None):
		self.id = id
		self.lc = lc
		self.rc = rc

class Tree:

	def __init__(self, root=None):
		self.root = root

	def insert_tree(self, key):
		new_node = Node(key)
		new_node.lc = None
		new_node.rc = None

		if self.root == None:
			self.root = new_node
		else:
			current = self.root
			while True:
				parent = current
				if key < current.id:
					current = current.lc
					if current == None:
						parent.lc = new_node
						return
				else:
					current = current.rc
					if current == None:
						parent.rc = new_node
						return
	
	def preorder_recursion(self, tree, new_tree):
		if tree:
			self.preorder_recursion(tree.lc, new_tree)
			print tree.id
			new_tree.insert_tree(tree.id)
			self.preorder_recursion(tree.rc, new_tree)


					




test = LinkedList()
test.insert(20)
test.insert(10)
test.insert(30)
#test.display_link()
test2 = LinkedList()

test1 = Tree()
test1.insert_tree(10)
test1.insert_tree(5)
test1.insert_tree(12)
test1.insert_tree(3)
test1.insert_tree(6)
test1.preorder_recursion(test1.root, test2)


