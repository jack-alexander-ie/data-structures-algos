import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max = 0
    min = 0

    for number in ints:

        if number >= max:
            max = number

        if number <= min:
            min = number

    return min, max


# Example Test Case of Ten Integers

list_of_ints = [i for i in range(0, 100)]  # a list containing 0 - 9

random.shuffle(list_of_ints)

print("Pass" if ((0, 99) == get_min_max(list_of_ints)) else "Fail")
