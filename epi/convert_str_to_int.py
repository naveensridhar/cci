def to_int(s):
    if s[0] == "-":
        is_negative = True
        start_char = 1
    else:
        is_negative = False
        start_char = 0
    numb = 0
    for i in range(start_char, len(s)):
        digit = ord(s[i]) - ord('0')
        numb = numb * 10 + digit
    if is_negative:
        numb = -numb

    return numb


print to_int("-21234")
