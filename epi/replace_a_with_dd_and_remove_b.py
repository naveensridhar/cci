def replace_operation(inp, size):
    a_count = 0
    curr_count = 0
    # Iterate front and remove 'b'
    for i in range(0, size):
        if inp[i] != 'b':
            inp[curr_count] = a[i]
            curr_count += 1
        if a[i] == 'a':
            a_count += 1
    #  Iterate back and add 'd's in place of 'a'
    total_count = curr_count + a_count - 1
    final_size = total_count
    while total_count >= 0:
        if inp[curr_count] == 'a':
            a[total_count] = 'd'
            a[total_count - 1] = 'd'
            total_count -= 2
        else:
            a[total_count] = a[curr_count]
            total_count -= 1
        curr_count -= 1
    return final_size




a = ['a', 'c', 'd', 'b', 'b', 'c', 'a']
#print replace_operation(a, len(a))
for i in range(0, replace_operation(a, len(a))):
    print a[i]
