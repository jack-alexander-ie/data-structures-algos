from typing import List


def test_ints(*numbers):
    """ Tests values to make sure they're integers, exits if any are not """
    for number in numbers:
        if type(number) is not int:
            print('Warning: Element tested that is not an integer, exiting...')
            exit()


def rotated_array_search(input_list: List[int], target: int) -> int:
    """
    Searches for an element in a rotated array

    :param input_list: list of integers to search
    :param target: the number to search for
    :return: the index of the target in the array, if found
    """
    test_ints(target)                                                   # Test target variable to ensure it's an int
    if input_list is None or len(input_list) is 0:                      # Tests if the list is empty
        return -1
    piv_idx = find_pivot(input_list)                                    # Finds the pivot index
    arr_one = input_list[:piv_idx]                                      # Grabs elements until the pivot index
    arr_two = input_list[piv_idx:]                                      # Grabs from the pivot index
    arr_one_idx = bin_search_rec(arr_one, target, 0, len(arr_one) - 1)  # Returns index of target if found
    if input_list[arr_one_idx] is target:                               # Found in arr_one, return it's index
        return arr_one_idx
    else:                                                               # If not, search for it in arr_two
        arr_two_idx = bin_search_rec(arr_two, target, 0, len(arr_two) - 1)
        if arr_two_idx == -1:
            return -1                                                   # Not found in either, return -1
        return len(arr_one) + arr_two_idx                               # Found in arr_two, return it's adjusted index


def find_pivot(list_nums: List[int]) -> int:
    """
    Performs binary search to find the pivot index of a rotated array, if one exists.

    :param list_nums: list of numbers in which to find the pivot
    :return: the index position of the pivot
    """
    if list_nums[0] <= list_nums[- 1]:                                # Test if list is rotated, return its midpoint
        return len(list_nums) - 1 // 2
    low, high = 0, len(list_nums) - 1
    while low <= high:
        mid = (low + high) // 2
        test_ints(list_nums[low], list_nums[mid], list_nums[high])    # Ensure pivot element is an integer
        if list_nums[mid] > list_nums[mid + 1]:                       # If centre val > value to it's right...
            return mid + 1                                            # ...return index of element to its right
        elif list_nums[low] <= list_nums[mid]:                        # Move right
            low = mid + 1
        else:
            high = mid - 1                                            # Move left


def bin_search_rec(array: List[int], target: int, start_index: int, end_index: int) -> int:
    """ Performs recursive binary search to seek target """
    centre_index = (start_index + end_index) // 2                     # Grab centre index
    centre_val = array[centre_index]                                  # Grab it's value
    test_ints(centre_val)                                             # Test if value's an integer
    if target == centre_val:                                          # If centre is the target, return it
        return centre_index
    if start_index <= end_index:                                      # Move start and end 'window'
        if target < centre_val:                                       # If target < centre val...
            end_index = centre_index - 1                              # ...move left
        else:                                                         # ...move right
            start_index = centre_index + 1
        return bin_search_rec(array, target, start_index, end_index)  # Keep searching
    return -1                                                         # Not found, return -1


# Test Cases - All pass
print("Pass" if (0 == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6)) else "Fail")
print("Pass" if (5 == rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1)) else "Fail")
print("Pass" if (2 == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8)) else "Fail")
print("Pass" if (3 == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1)) else "Fail")
print("Pass" if (-1 == rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10)) else "Fail")

# Test Case - Array not rotated
print("Pass" if (0 == rotated_array_search([1, 2, 3, 4, 5, 6, 7], 1)) else "Fail")

# Test Case - Non-integer target
# rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 'a')
# Expected: 'Warning: Element tested that is not an integer, exiting...'

# Test Case - Element in the list is not an integer
# rotated_array_search([6, 7, 8, 9, 'c', 1, 2, 3, 4], 6)
# Expected: 'Warning: Element tested that is not an integer, exiting...'
