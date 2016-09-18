def reverse(s):
    if len(s) == 1:
        return s

    out = reverse(s[1:]) + s[0]
    return out


def reverse_sentence(sent):
    a = sent.split(" ")
    new_string = ""
    for i in a:
        if new_string == "":
            new_string =  reverse(i)
        else:
            new_string = new_string + " " + reverse(i)
    return reverse(new_string)
print reverse("test")
print reverse_sentence("Naveen testing this")
