def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    out = []
    alength = len(a)
    blength = len(b)
    sum = 0
    for i in range(0, max(alength, blength)):
        if i < alength and a[alength-1-i] == '1':
            sum = sum + 1
        if i < blength and b[blength-1-i] == '1': 
            sum = sum + 1
        out.append(str(sum%2))
        sum /= 2
    if sum > 0:
        out.append(str(sum%2))
    return "".join(out)

print addBinary("1", "0")
