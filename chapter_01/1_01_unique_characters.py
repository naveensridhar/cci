def unique_char(input):
    if len(input) > 256:
        return False
    uniq = set()
    for i in input:
        if i in uniq:
            return False
        uniq.add(i)
    return True     
print unique_char("iates")
