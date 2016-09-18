
def sum(a, b):
    if a < 0:
        a = ~a
    if b < 0:
        b = ~b
    while (b != 0):
        c = a&b
        a= a^b
        b= c<<1
    return a

print sum(4, -2)
