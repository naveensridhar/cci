import random
def quick_sort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quick_sort(A, l, p-1)
        quick_sort(A, p+1, r) 

def partition(A, l, r):
    pivot=random.randint(l, r)
    A[l], A[pivot] = A[pivot], A[l]
    j = l+1
    for i in range(l+1, r+1):
        if A[i] < A[l]:
            A[j], A[i] = A[i], A[j]
            j += 1
    A[l], A[j-1] = A[j-1], A[l]
    return j-1

input = [10, 20, 30, 8, 5, 4, 15]
quick_sort(input, 0, len(input)-1)        
print input
            
