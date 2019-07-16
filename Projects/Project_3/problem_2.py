from typing import List


def rotated_array_search(input_list: List[int], number: int) -> int:

    if type(number) is not int:
        print('Warning: The target value must be an integer')
        return -1

    for element in input_list:          # Single traversal afforded as it will not add hugely to time complexity
        if type(element) is not int:
            print('Warning: One or more of the elements in the list is not an integer')
            return -1

    if input_list is None or len(input_list) is 0:
        return -1

    pivot_index = find_pivot(input_list)
    array_one, array_two = input_list[:pivot_index], input_list[pivot_index:]
    result_one = binary_search_recursive(array_one, number, 0, len(array_one) - 1)

    if input_list[result_one] == number:
        return result_one
    else:
        result_two = binary_search_recursive(array_two, number, 0, len(array_two) - 1)
        if result_two == -1:
            return -1
        return len(array_one) + result_two


def find_pivot(list_of_nums: List[int]) -> int:

    if list_of_nums[0] <= list_of_nums[len(list_of_nums) - 1]:  # Check to see if list is rotated
        return 0

    low, high = 0, len(list_of_nums) - 1

    while low <= high:
        mid = (low + high)//2
        if list_of_nums[mid] > list_of_nums[mid+1]:
            return mid + 1
        elif list_of_nums[low] <= list_of_nums[mid]:
            low = mid + 1
        else:
            high = mid - 1


def binary_search_recursive(array: List[int], target: int, start_index: int, end_index: int) -> int:

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


# Test Cases - All pass
# print("Pass" if (0 == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)) else "Fail")
# print("Pass" if (5 == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)) else "Fail")
# print("Pass" if (2 == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8)) else "Fail")
# print("Pass" if (3 == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1)) else "Fail")
# print("Pass" if (-1 == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10)) else "Fail")

# Test Case - Non-integer target
# rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 'a')
# Expected: 'Warning: The target value must be an integer'

# Test Case - Element in the list is not an integer
# rotated_array_search([6, 7, 8, 9, 'c', 1, 2, 3, 4], 6)
# Expected: 'Warning: One or more of the elements in the list is not an integer'
