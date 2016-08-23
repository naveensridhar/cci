
def string_reverse(input):
    s = []
    for i in input:
        if i != "\n":
            s.append(i)
    l = len(s)
    for j in range(0, l):
        print s.pop()

string_reverse("naveen\n")
