def next_number(s):
    count = 0
    new_str = ""
    prev_char = s[0]
    for i in range(0, len(s)):
        if s[i] == prev_char:
            count += 1
        else:
            new_char = str(count) + prev_char
            new_str = new_str + new_char
            count = 1
            prev_char = s[i]
    new_char = str(count) + prev_char
    new_str = new_str + new_char
    return new_str

def lookandsay():
    curr = "1"
    for i in range(0, 7):
        curr = next_number(curr)
    print curr        
lookandsay()
