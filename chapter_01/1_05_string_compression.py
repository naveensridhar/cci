import sys
#Try to compress string. Example input: aaaabba output: a4b2a1 if compressed data is smaller than the input
def compress_string(input):
    char_counter = 0
    prev_char = input[0]
    new_str_list = []
    for i in input:
        if prev_char == i:
            char_counter = char_counter + 1
        else:
            new_str_list.append(prev_char)
            new_str_list.append(str(char_counter))
            prev_char = i
            char_counter = 1
    new_str_list.append(prev_char)
    new_str_list.append(str(char_counter))
    if len(new_str_list) < len(input):
        return "".join(new_str_list)
    return input

print compress_string(sys.argv[1])
