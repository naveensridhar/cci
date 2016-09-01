import sys
def replace_space(input):
    output_list = []
    str = ""
    for i in input:
        if i == " ":
            str = str + "%20"
        else:
            str = str + i
    return str

print replace_space(sys.argv[1])
