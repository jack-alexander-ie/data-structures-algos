def recursive_binary_search(target, source, left=0):

    if len(source) == 0:
        return None

    center = (len(source)-1) // 2

    if source[center] == target:
        return center + left

    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)

    else:
        return recursive_binary_search(target, source[:center], left)


def first_and_last_index(arr, number):
    """
        Given a sorted array that may have duplicate values, use binary
        search to find the first and last indexes of a given value.

        Args:
            arr(list): Sorted array (or Python list) that may have duplicate values
            number(int): Value to search for in the array
        Returns:
            a list containing the first and last indexes of the given value
        """

    if len(arr) == 1:           # Check to see if array has more than 1 element
        if arr[0] == number:
            return [0, 0]
        else:
            return [-1, -1]

    rec_index = recursive_binary_search(number, arr)    # Recursive call to find if element is in a list

    if not rec_index:
        return [-1, -1]

    start_index, end_index = rec_index, rec_index + 1

    if end_index == len(arr):
        end_index -= 1

    indexes = [start_index, end_index]

    # Find start index
    while arr[start_index] == number:

        if start_index == 0:
            break

        if arr[start_index - 1] == number:
            start_index -= 1

        else:
            break

    # Find end index
    while arr[end_index] == number:

        if end_index == len(arr):
            break

        if end_index + 1 == len(arr):
            break

        if arr[end_index + 1] == number:
            end_index += 1

        else:
            break

    return [start_index, end_index]


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)
