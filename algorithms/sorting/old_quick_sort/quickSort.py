import numpy
test = 0 

def swap(A, index1, index2):
	temp = A[index1]
	A[index1] = A[index2]
	A[index2] = temp

def findmedian(A, l, r):
	length = r - l + 1
	if length < 2:
		return 0
	if length%2 == 0:
		middIndex = length/2 - 1
	else:
		middIndex = length/2
	valTest = []

	valTest.append(A[l])
	valTest.append(A[middIndex])
	valTest.append(A[r])
	value = numpy.median(numpy.array(valTest))
	if A[l] == value:
		return l
	elif A[middIndex] == value:
		return middIndex
	else:
		return r

def partition(A, l, r):
	medIndex = findmedian(A, l, r)
	print medIndex
	swap(A, l, medIndex)
	global test
	test = test + (r - l)
	pivot = A[l]
	i = l + 1

	for j in range(l+1, r+1):
		if A[j] < pivot:
			swap(A, i, j)
			i = i + 1
	swap(A, l, (i-1))
	return i-1


def quickSort(A):
   quickSortHelper(A,0,len(A)-1)

def quickSortHelper(A,first,last):
   if first<last:

       splitpoint = partition(A,first,last)
       quickSortHelper(A,first,splitpoint-1)

       quickSortHelper(A,splitpoint+1,last)


#f = open("Quicksort.txt", "r")
#A = []
#for i in f.readlines():
#	val = i.rstrip('\n')
#	A.append(int(val))
A = [1,2,3,4,5,6,7,8,9]
quickSort(A)
print A
print test

