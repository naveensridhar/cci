import sys
# Find number of times each character occurs in first string. Then reduce the count by going through the second string
def anagram(string1, string2):

    if len(string1) != len(string2):
        return False
    dict_key = {}
    for i in string1:
        if i in dict_key:
            dict_key[i] = dict_key[i] + 1
        else:
            dict_key[i] = 1
    
    for j in string2:
        if j in dict_key:
            dict_key[j] = dict_key[j] -1 
            if dict_key[j] == 0:
                dict_key.pop(j)
        else:
            return False
    if len(dict_key) > 0:
        return False
    return True

string1 = sys.argv[1]
string2 = sys.argv[2]
print anagram(string1, string2)
    

