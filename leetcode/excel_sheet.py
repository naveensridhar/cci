def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    a = []
    while(n > 0):
        a.insert(0, chr(((n-1)/26)  + ord('A')))
        n = (n-1)/26
    return "".join(a)
print convertToTitle(28)

