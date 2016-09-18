def is_valid(s):
    if len(s) > 3:
        return False

    if len(s) > 0 and s[0] == '0':
        return False

    if int(s) < 0 or int(s) > 255:
        return False
    return True

def valid_ip_address(s):
    out = []
    for i in range(1, 4):
        first_part = s[0:i]
        if is_valid(first_part):
            for j in range(1, 4):
                 second_part = s[i:i+j]
                 if is_valid(second_part):
                     for k in range(1, 4):
                         third_part = s[i+j:i+j+k]
                         fourth_part = s[i+j+k:len(s)]
                         if is_valid(third_part) and is_valid(fourth_part):
                             valid = first_part + "." + second_part + "." + third_part + "." + fourth_part
                             print valid
                             out.append(valid)
         
    return out

print valid_ip_address("25525511135")                     
