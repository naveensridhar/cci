class Node:
	def __init__(self, id= None, lc=None, rc=None):
		self.id = id
		self.lc = lc
		self.rc = rc


class Tree:
	def __init__(self, root=None):
		self.root = root

	def insert_tree(self, key):
		new_node = Node(key)
		if self.root == None:
			self.root = new_node
		else:
			parent = self.root
			while True:
				current = parent
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

				parent = current


	def preorder_recursion(self, tree):
		if tree:
			self.preorder_recursion(tree.lc)
			print tree.id
			self.preorder_recursion(tree.rc)


test1 = Tree()
test1.insert_tree(10)
test1.insert_tree(5)
test1.insert_tree(12)
test1.insert_tree(3)
test1.insert_tree(6)
test1.preorder_recursion(test1.root)

