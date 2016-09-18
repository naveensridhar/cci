def find_nth(A, l, r, k):
    if l <= r:
        p = partition(A, l, r)
        if p == k:
            return A[p]
        elif k > p:
            return find_nth(A, p+1, r, k)
        else:
            return find_nth(A, l, p-1, k)

def partition(A, l, r):
    import random
    pivot = random.randint(l, r)
    A[l], A[pivot] = A[pivot], A[l]
    j = l+1
    for i in range(l+1, r+1):
        if A[i] < A[l]:
            A[i], A[j] = A[j], A[i]
            j += 1

    A[j-1], A[l] = A[l], A[j-1]
    return j-1

A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print find_nth(A, 0, len(A)-1, 4)

                
