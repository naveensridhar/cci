def binary_search(A, k):
    result = -1
    left = 0
    right = len(A) - 1
    while(left <= right):
        mid = left + ((right - left)/2)
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
print binary_search(A, 285)
