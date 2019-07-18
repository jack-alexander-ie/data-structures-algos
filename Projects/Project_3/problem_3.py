from typing import List


def test_list(list_ints: List[int]) -> bool:
    """ Checks all elements in a list to ensure they're all integers """
    for element in list_ints:          # O(n) traversal afforded -> will not add significantly to time complexity
        if type(element) is not int:
            print('Warning: One or more of the elements in the list is not an integer')
            return True
    return False


def merge_sort(arr: List[int]) -> None:
    """ Performs a merge sort to sort the numbers in an array """
    if len(arr) > 1:
        mid = len(arr) // 2                                  # Find the mid of the array
        left_array, right_array = arr[:mid], arr[mid:]       # Divide array elements into 2 halves

        merge_sort(left_array)                               # Sort the first half
        merge_sort(right_array)                              # Sort the second half

        i = j = k = 0                                        # Set tracking variables

        while i < len(left_array) and j < len(right_array):  # Copy data to temporary arrays
            if left_array[i] < right_array[j]:               # If left < right element...
                arr[k] = left_array[i]                       # ...replace kth value in input array
                i += 1                                       # Move right in temporary left-hand array
            else:
                arr[k] = right_array[j]                      # Right < left, replace kth value in input array
                j += 1                                       # Move right in temporary right-hand array
            k += 1                                           # Bump kth index up one

        # 2 x (1. Check if elements remain, 2. add spares to temp array, 3. increase trackers)
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1


def rearrange_digits(input_list: List[int]) -> List[int]:
    """ Rearranges array elements to form two numbers such that their sum is the maximum """
    if test_list(input_list): return [0, 0]                  # 1. Test if list values are all ints, return if not
    merge_sort(input_list)                                   # 2. Merge sort the input list
    reverse_list(input_list)                                 # 3. Sort list in descending order
    return find_max_pair(input_list)                         # 4. Return max pair


def reverse_list(list_of_nums: List[int]) -> None:
    """ Reverses elements of list in-place """
    for i in range(len(list_of_nums)):
        number = list_of_nums.pop()
        list_of_nums.insert(i, number)


def find_max_pair(input_list: List[int]) -> List[int]:
    """ Finds and returns the pair with the maximum value """
    str_1, str_2 = '', ''
    index = 0
    while index <= len(input_list) + 1:
        str_1 += str(input_list.pop(0))
        if len(input_list) > 0:
            str_2 += str(input_list.pop(0))
        index += 1
    return [int(str_1), int(str_2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test Cases - Both should pass
# test_function([[1, 2, 3, 4, 5], [542, 31]])         # Expected output: Pass
# test_function([[4, 6, 2, 5, 9, 8], [964, 852]])     # Expected output: Pass

# Test Case - Non-integer input
# test_function([[1, 2, 'a', 4, 5], [542, 31]])
# Expected output: Warning: One or more of the elements in the list is not an integer

# Test Case - Large Input
# test_arr, rotation_index = [number for number in range(1, 36)], 15
# test_rotated_arr = test_arr[rotation_index:] + test_arr[:rotation_index]
# print(test_rotated_arr)
# print(rearrange_digits(test_rotated_arr))
# Expected Output: [35333129272523211917151311, 34323028262422201816141210]
