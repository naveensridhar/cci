import sys
def string_rotation(s1, s2):
    if len(s2) != len(s1):
        return False
    #s2 is definiteley a substring of s1s2
    new_string = s1 + s1
    print new_string
    print s2
    return s2 in new_string

print string_rotation(sys.argv[1], sys.argv[2])
