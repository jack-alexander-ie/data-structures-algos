def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad_new(number):

    if number <= 1:
        return [""]
    elif number <= 9:
        # Only triggered on last digit - all previous numbers are too big
        return list(get_characters(number))

    last_digit = number % 10
    init_output = keypad_new(number//10)

    letters = get_characters(last_digit)

    output = list()

    for letter in letters:

        for sub_perm in init_output:

            new_perm = sub_perm + letter
            output.append(new_perm)

    return output


print(keypad_new(234))
