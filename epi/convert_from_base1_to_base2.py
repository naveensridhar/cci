def convert_base(s, b1, b2):
    is_negative = 1 if s[0] == '-' else 0
    a = {}
    a[0] = "0"
    a[1] = "1"
    a[2] = "2"
    a[3] = "3"
    a[4] = "4"
    a[5] = "5"
    a[6] = "6"
    a[7] = "7"
    a[8] = "8"
    a[9] = "9"
    a[10] = "A"
    a[11] = "B"
    a[12] = "C"
    a[13] = "D"
    a[14] = "E"
    a[15] = "F"
    
    num = 0
    for i in range(1 if is_negative else 0, len(s)):
        digit = ord(s[i]) - ord("0")
        num = num*b1 + digit
    out = ""
    while(num > 0):
        rem = num%b2
        out = a[rem] + out
        num = num/b2

    out = "-" + out if is_negative else out
    print out

convert_base("123", 10, 16)

