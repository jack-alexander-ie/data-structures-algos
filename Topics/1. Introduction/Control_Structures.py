
def smallest_positive_jack(in_list):
    # TODO: Define a control structure that finds the smallest positive number
    #       in in_list and returns the correct smallest number.

    positive_integers = [i for i in in_list if i >= 0]

    # Can also randomly allocate int to compare against
    smallest_integer = positive_integers[0]

    for j in positive_integers:
        if j < smallest_integer:
            smallest_integer = j

    return smallest_integer

    # Alternative one liner
    # return min(i for i in in_list if i > 0)


# Test cases

# print(smallest_positive_jack([4, -6, 7, 2, -4, 10]))
# Correct output: 2

# print(smallest_positive_jack([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2


def smallest_positive(in_list):

    smallest_integer = None

    for number in in_list:

        if number > 0:

            # None valuation only works on first iteration, like setting a positive var on the first round
            if smallest_integer is None or number < smallest_integer:

                smallest_integer = number

    return smallest_integer

# Test cases


# print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

# print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

def tester(n):

    smallest = None

    return n < None


# print(tester(2))

