def add_one(digits):

    a = len(digits)
    carry = 1
    for i in range(a-1, -1, -1):
        sum = digits[i] + carry
        digits[i] = sum%10
        carry = sum/10
    
    if carry > 0:
        digits = [1] + digits
    return digits

a = [1, 0]
print add_one(a)
