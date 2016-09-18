def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while(i<j):
        while(not(s[i].isalnum()) and (i<j)):
            i += 1
        while(not(s[j].isalnum()) and (i<j)):
            j -= 1
        if s[i].upper() != s[j].upper():
            return False
        i += 1
        j -= 1
    return True



print is_palindrome("Madam,")
print is_palindrome("aadam,")
print is_palindrome("A man, a plan, a canal, Panama")  
print is_palindrome(".,")   
