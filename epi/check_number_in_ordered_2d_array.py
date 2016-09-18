def check_value(A, k):
    left = 0
    right = len(A[0]) - 1
    while(left < len(A) and right >= 0):
        if A[left][right] < k:
            right = right-1
        elif A[left][right] > k:
            left = left + 1
        else:
            return left, right
    return False

A = [[-1, 2, 4, 4, 6], [1, 5, 5, 9, 21], [3, 6, 6, 9, 22] , [3, 6, 8, 10, 24], [6, 8, 9, 12, 25], [8, 10, 12, 13, 40]]
print len(A)
print check_value(A, 7)
print check_value(A, 6)
