def rotated_array_search(input_list, number):

    if input_list is None or len(input_list) is 0:
        return -1

    pivot_index = find_pivot(input_list)

    array_one = input_list[:pivot_index]
    array_two = input_list[pivot_index:]

    result_one = binary_search_recursive(array_one, number, 0, len(array_one) - 1)

    if input_list[result_one] == number:
        return result_one
    else:
        result_two = binary_search_recursive(array_two, number, 0, len(array_two) - 1)

        if result_two == -1:
            return -1

        return len(array_one) + result_two


def find_pivot(list_of_nums):

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


def binary_search_recursive(array, target, start_index, end_index):

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


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
