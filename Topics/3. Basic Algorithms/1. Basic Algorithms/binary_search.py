"""
Binary Search Implementations

How the algorithm works:

    1. Find the center of the list (try setting an upper and lower bound to find the center)
    2. Check to see if the element at the center is your target.
    3. If it is, return the index.
    4. If not, is the target greater or less than that element?
    5. If greater, move the lower bound to just above the current center
    6. If less, move the upper bound to just below the current center
    7. Repeat steps 1-6 until you find the target or until the bounds are the same or
       cross (the upper bound is less than the lower bound).
"""


# Iterative solution
def binary_search(array: list, target: int) -> int:
    """
    Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:

        centre_index = (start_index + end_index)//2
        test_val = array[centre_index]

        if target == test_val:
            return centre_index

        elif target < test_val:
            end_index = centre_index - 1

        else:
            start_index = centre_index + 1

    return -1


# def test_function(test_case):
#     answer = binary_search(test_case[0], test_case[1])
#     if answer == test_case[2]:
#         print("Pass!")
#     else:
#         print("Fail!")
#
#
# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 6
# index = 6
# test_case = [array, target, index]
# test_function(test_case)


def binary_search_recursive(array, target, start_index, end_index):
    """
    Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """

    centre_index = (start_index + end_index) // 2
    test_val = array[centre_index]

    if target == test_val:
        return centre_index

    if start_index <= end_index:
        if target < test_val:
            end_index = centre_index - 1
        else:
            start_index = centre_index + 1
        return binary_search_recursive(array, target, start_index, end_index)
    return -1


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1], test_case[3], test_case[4])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 1
index = 1
start_index = 0
end_index = len(array) - 1

test_case = [array, target, index, start_index, end_index]
test_function(test_case)
