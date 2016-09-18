def move_zeroes(A):
    size = len(A)
    pos = 0
    for i in range(0, size):
        if A[i] != 0:
            A[pos] = A[i]
            pos += 1

    for j in range(size-1, pos-1, -1):
        A[j] = 0

    return A

A = [10, 5, 0, 0, 4, 5, 6, 8]
print move_zeroes(A)
