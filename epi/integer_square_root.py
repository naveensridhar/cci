def closest_square_root(k):
    left = 0
    right = k
    while(left <= right):
        mid = left + ((right-left)/2)
        mult = mid * mid
        if mult <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

print closest_square_root(300)    
