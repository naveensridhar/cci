def contain_duplicate(nums):
    hash_lookup = {}
        
    for item in nums:
        if item in hash_lookup:
            return True
        else:
            hash_lookup[item] = 1
            
    return False

a = [2, 3, 2]
print contain_duplicate(a)
