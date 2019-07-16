from typing import List


def merge_sort(arr: List[int]):
    """ Executes a merge sort to sort the numbers in an array """
    if len(arr) > 1:
        mid = len(arr) // 2         # Find the mid of the array
        left_array = arr[:mid]      # Divide the array elements
        right_array = arr[mid:]     # into 2 halves

        merge_sort(left_array)       # Sort the first half
        merge_sort(right_array)      # Sort the second half

        i = j = k = 0

        while i < len(left_array) and j < len(right_array):    # Copy data to temp arrays
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):    # Check if any elements remain
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):   # Check if any elements remain
            arr[k] = right_array[j]
            j += 1
            k += 1


def rearrange_digits(input_list: List[int]) -> List[int]:
    """ Rearranges array elements to form two numbers such that their sum is the maximum """
    for element in input_list:          # O(n) traversal afforded -> will not add significantly to time complexity
        if type(element) is not int:
            print('Warning: One or more of the elements in the list is not an integer')
            return [0, 0]
    merge_sort(input_list)              # 1. Sort the input list - O(n log n)
    reverse_list(input_list)            # 2. Sort list in descending order - O(n)
    return find_max_pair(input_list)    # 3. Return max pair - O(n)


def reverse_list(list_of_nums: List[int]):
    """ Executes in-place reversal of elements """
    for i in range(len(list_of_nums)):
        number = list_of_nums.pop()
        list_of_nums.insert(i, number)


def find_max_pair(input_list: List[int]) -> List[int]:
    """ Finds and return the pair with the maximum value """
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
