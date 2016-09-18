def smallest_element(A):
    left = 0
    n = len(A) - 1
    right = n
    while(left<right):
        mid = left + ((right-left)/2)
        if A[mid] > A[n]:
            left = mid + 1
        else:
            right = mid
    return left
A = [4, 5, 6, 7, 8, 9, 1, 2, 2, 4, 5]
print smallest_element(A)
