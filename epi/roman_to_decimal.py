roman_map = {}
roman_map["I"] = 1
roman_map["V"] = 5
roman_map["X"] = 10
roman_map["L"] = 50
roman_map["C"] = 100
roman_map["D"] = 500
roman_map["M"] = 1000

def roman_to_decimal(s):
    l = len(s) - 1
    prev_char = s[l]
    sum = roman_map[prev_char]
    if l == 0:
        return sum
    print l
    for i in range(l-1, -1, -1):
        print s[i]
        if roman_map[prev_char] > roman_map[s[i]]:
            sum -= roman_map[s[i]]
        else:
            sum += roman_map[s[i]]
        prev_char = s[i]
    return sum

print roman_to_decimal("XVV")
