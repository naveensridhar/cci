def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    def reverse(nums, start, stop):
        for i in range(start, start+(stop-start+1)/2):
            nums[i], nums[start+stop-i] = nums[start+stop-i], nums[i]
            
    l = len(nums)
    shift = l-k-1
    if l > 1:
        reverse(nums, 0, shift)
        reverse(nums, shift+1, l-1)
        reverse(nums, 0, l-1)
nums = [1,2,3,4,5,6]
k = 11%len(nums) 
rotate(nums, k)
print nums
