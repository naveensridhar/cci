class Heap:

	def __init__(self, current_size=0, pqueue=None):
		self.current_size = -1
		self.pqueue = []

	def trickle_up(self, n):
		while (n-1)/2 >= 0:
			if self.pqueue[n] > self.pqueue[(n-1)/2]:
				self.pqueue[n], self.pqueue[(n-1)/2] = self.pqueue[(n-1)/2], self.pqueue[n]
				n = (n-1)/2
			else:
				return

	def maxChild(self, i):
		lc = i*2 + 1
		rc = i*2 + 2
		if lc and rc < self.current_size:
			return i*2
		if self.pqueue[lc] > self.pqueue[rc]:
			return  lc
		else:
			return  rc

	def trickle_down(self):
		n = 0
		while n*2 + 1  < self.current_size:
			mc = self.maxChild(n)
			if self.pqueue[n] < self.pqueue[mc]:
				self.pqueue[n], self.pqueue[mc] = self.pqueue[mc], self.pqueue[n]
				n = 2*n + 1
			else:
				return



	def insert(self, id):
		self.pqueue.append(id)
		self.trickle_up(self.current_size)
		self.current_size = self.current_size + 1


	def delete(self):
		tmp = self.pqueue[0]
		print tmp
		self.pqueue[0] = self.pqueue[self.current_size]
		self.pqueue.pop()
		self.current_size = self.current_size - 1
		self.trickle_down()
		return tmp


theHeap = Heap()
theHeap.insert(70)
theHeap.insert(40)
theHeap.insert(50)
theHeap.insert(20)
theHeap.insert(60)
theHeap.insert(100)
theHeap.insert(80)
theHeap.insert(30)
theHeap.insert(10)
theHeap.insert(90)
print theHeap.pqueue
print theHeap.current_size
a = []
test = len(theHeap.pqueue)
for i in range(test):
	a.append(theHeap.delete())
print a
