def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    while(m>0 and n>0):
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
            
    while (n>0):
        nums1[m+n-1] = nums2[n-1]
        n -= 1
    print A

A = [1, 3, 5, 7, 10, 0, 0, 0, 0, 0]
B = [2, 4, 5, 8, 11]
merge(A, 5, B, 5)
