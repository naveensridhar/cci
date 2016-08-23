def merge_sort(inp):
	if len(inp) == 1:
		return inp
	n = len(inp)
	left = merge_sort(inp[:n/2])
	right = merge_sort(inp[n/2:])
	i = 0
	j = 0
	c = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			c.append(left[i]) 
			i = i + 1
		elif left[i] >= right[j]:
			c.append(right[j]) 
			j = j + 1
	if i < len(left):
		for iin in range(i, len(left)):
			c.append(left[iin])
	if j < len(right):
		for jin in range(j, len(right)):
			c.append(right[jin]) 
	return c

input = [100, 30, 20]
print merge_sort(input)