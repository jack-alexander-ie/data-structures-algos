def reverse_string(input):

    # Base Case - when string is empty
    if len(input) == 0:
        return ""

    # Recursive Case - last char + input char
    return reverse_string(input[1:]) + input[0]


print(reverse_string('cba'))
