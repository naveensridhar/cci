class Node:
	def __init__(self, id, lc=None, rc=None):
		self.id = id
		self.lc = lc
		self.rc = rc

class Tree:
	def __init__(self, root=None):
		self.root = root

	def insert_node(self, k=None):
		new_node = Node(k)
		new_node.lc = None
		new_node.rc = None
		if self.root == None:
			self.root = new_node
		else:
			current = self.root
			while True:
				parent = current
				if k < current.id:
					current = current.lc
					if current == None:
						parent.lc = new_node
						return
				else:
					current = current.rc	
					if current == None:
						parent.rc = new_node
						return


	def preorder(self, tree):
		if tree:
			self.preorder(tree.lc)
			print tree.id

			self.preorder(tree.rc)

	def display(self):
		self.preorder(self.root)

test = Tree()
test.insert_node(10)
test.insert_node(5)
test.insert_node(12)
test.insert_node(3)
test.insert_node(6)

test.display()


