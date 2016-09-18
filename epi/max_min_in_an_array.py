def max_min(a, b):
    return (a,b) if a >b else (b,a)

def find_max_min(A):
    l = len(A)
    if l <= 1:
        return (A[0], A[0]) 
    if l%2 == 0:
        max, min = max_min(A[0], A[1])
        start = 2
    else:
        max, min = (A[0], A[0]) 
        start = 1

    if l == 2:
        return max, min

    for i in range(start, l-1, 2):
        local_max, local_min = max_min(A[i], A[i+1])
        max = max_min(local_max, max)[0]
        min = max_min(local_min, min)[1]
    return max, min


A = [3, 10, 4, 7, 8, 9, 10, 1]  
print find_max_min(A)
B = [0, 3, 10, 4, 7, 8, 9, 10, 1, 3]
print find_max_min(B)
