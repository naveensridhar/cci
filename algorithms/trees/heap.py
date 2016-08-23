

class Heap:

	def __init__(self):
		self.current_size = 0
		self.heap_list = []


	def maxchild(self, i):
		if self.heap_list[i*2 + 1] > self.heap_list[i*2 + 2]:
			return  i*2 + 1
		else:
			return  i*2 + 2


	def trickle_down(self, i):
		while (i * 2 <= self.current_size - 1):
			mc = self.maxchild(i)
			if self.heap_list[i] < self.heap_list[mc]:
				self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
				i = i*2 + 1
			else:
				return
	
	def trickle_up(self, i):
		while ((i-1)//2) >= 0:
			if self.heap_list[i] > self.heap_list[((i-1)//2)]:
				self.heap_list[((i-1)//2)], self.heap_list[i] = self.heap_list[i], self.heap_list[((i-1)//2)]
				i = ((i-1)//2)
			else:
				return
		

	def insert(self, k):
		self.heap_list.append(k)
		self.current_size = self.current_size + 1
		self.trickle_up(self.current_size -1)

	def delete(self):
		tmp  = self.heap_list[0]
		self.heap_list[0] = self.heap_list[len(self.heap_list)-1]
		self.heap_list.pop()
		self.current_size = self.current_size - 1
		self.trickle_down(0)
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

print theHeap.heap_list
theHeap.delete()
print theHeap.heap_list

