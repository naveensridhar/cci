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


	def compare(self, tree1, tree2):
		if tree1 == None and tree2 == None:
			return True
		else:
			if tree1 != None and tree2 != None:
				return (tree1.id == tree2.id and self.compare(tree1.lc, tree2.lc) and self.compare(tree1.rc, tree2.rc))
			else:
				return False

	def display(self):
		self.preorder(self.root)

test1 = Tree()
test1.insert_node(10)
test1.insert_node(5)
test1.insert_node(12)
test1.insert_node(3)
test1.insert_node(6)

test2 = Tree()
test2.insert_node(10)
test2.insert_node(12)
test2.insert_node(5)
test2.insert_node(3)
test2.insert_node(6)
test2.insert_node(6)

print test1.compare(test1.root, test2.root)


