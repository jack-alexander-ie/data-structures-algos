from typing import List, Tuple


def test_int(number):
    if type(number) != int:
        print('Warning: Cannot compare a value that is not an integer')
        return False
    return True


def get_min_max(ints: List[int]) -> Tuple[int, int]:
    """ Returns a tuple (min, max) out of list of unsorted integers. """
    if len(ints) < 1:
        print('Warning: Cannot operate on an empty list')
        return 0, 0
    min_val, max_val = ints[0], ints[0]         # Choose two random values from the list
    for number in ints:                         # Iterate over the list to find min and max
        if not test_int(number): return 0, 0    # Test each value to make sure it's an integer
        if number >= max_val:
            max_val = number
        if number <= min_val:
            min_val = number
    return min_val, max_val


# Test Case - Correct answer
# list_of_ints = [i for i in range(1, 101)]  # a list containing 1 - 100
# random.shuffle(list_of_ints)
# print("Pass" if ((1, 100) == get_min_max(list_of_ints)) else "Fail")     # Expected: Pass

# Test Case - Invalid string input
# list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 'nine']
# get_min_max(list_of_ints)                       # Expected: 'Warning: Cannot compare a value that is not an integer'

# Test Case - Empty input
# list_of_ints = []
# get_min_max(list_of_ints)                       # Expected: 'Warning: Cannot operate on an empty list'

# Test Case - two identical numbers
# list_of_ints = [10, 10]
# print("Pass" if ((10, 10) == get_min_max(list_of_ints)) else "Fail")     # Expected: Pass
