def reverse(s):
    j = len(s) - 1
    for i in range(0, len(s)+1):
        s[i], s[j] = s[j], s[i]
        j += 1
    

    return s

print reverse("resr")
