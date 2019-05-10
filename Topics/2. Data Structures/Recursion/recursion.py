
def sum_integers(n):
    """

        Each function waits on the function it called to complete.

        e.g. sum_integers(5)

        The function sum_integers(1) will return  1, then feedback:

            sum_integers(2) returns 2 + 1
            sum_integers(3) returns 3 + 3
            sum_integers(4) returns 4 + 6
            sum_integers(5) returns 5 + 10

    """

    # Base Case
    if n == 1:
        return 1

    return n + sum_integers(n - 1)


# Works
# print(sum_integers(5))

# Doesn't work
# print(sum_integers(1000))


"""
    Python has a limit on the depth of recursion to prevent a stack overflow. However, some compilers will turn 
    tail-recursive functions into an iterative loop to prevent recursion from using up the stack. Since Python's 
    compiler doesn't do this, watch out for this limit.
    
    Tail-recursive functions are functions in which all recursive calls are tail calls and hence do not build up 
    any deferred operations.
    
    Each call to factorial generates a new stack frame. The creation and destruction of these stack frames is what 
    makes the recursive factorial slower than its iterative counterpart.

"""


def power(n):

    """

    Each function waits on the function it called to complete.

    e.g. 2^5

    The function power_of_2(0) will return  1:

        1 returned from power_of_2(0), power_of_2(1) returns 2∗1
        2 returned from power_of_2(1), power_of_2(2) returns 2∗2
        4 returned from power_of_2(1), power_of_2(2) returns 2∗4
        8 returned from power_of_2(1), power_of_2(2) returns 2∗8
        16 returned from power_of_2(4), power_of_2(5) returns 2∗16

    """

    if n == 0:
        return 1

    return 2 * power(n - 1)


# Works
# print(power(5))

# Causes max recursion depth error
# print(power(1000))


def factorial(n):

    if n == 0 or n == 1:
        return 1

    previous = factorial(n-1)
    return n * previous


# print(factorial(5))

"""
    Slicing Arrays
"""


# Not particularly time or space efficient
def sum_array(array):

    # Base Case - when down to it's last element
    if len(array) == 1:
        return array[0]

    # Recursive case - keep burrowing
    return array[0] + sum_array(array[1:])


# print(sum_array([1, 2, 3, 4, 5, 6]))


def sum_array_index(array, index):

    """
    Instead of slicing, pass the index for the element needed for addition.
    """

    # Base Case - when the end of the array is reached
    if len(array) - 1 == index:
        return array[index]

    # Recursive Case - Same array passed in each time but index is incremented to grab values
    return array[index] + sum_array_index(array, index + 1)


print(sum_array_index([1, 2, 3, 4, 5, 6], 0))
