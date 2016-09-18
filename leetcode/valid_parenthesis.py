def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    dict = {"{": "}", "[": "]", "(":")"}
    storage_stack = []
    for i in s:
        if i in dict:
            storage_stack.append(i)
        else:
            if storage_stack == [] or dict[storage_stack.pop()] != i:
                return False
    print storage_stack
    if len(storage_stack) > 0:
        return False
    else:
        return True
print isValid("()")
