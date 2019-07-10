"""
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use
any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an
O(n) solution but it will not count as single traversal.
"""


def sort_012(input_list: list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start, mid, pivot = 0, 0, 1
    end = len(input_list) - 1

    last_zero_idx, last_one_idx, last_two_idx = 0, 0, 0

    for number in

    while mid <= end:

        if input_list[mid] < pivot:     # current element is 0

            # Pop it out and insert it at the front
            temp = input_list.pop(mid)
            input_list.insert(0, )

            temp = input_list[start]
            input_list[start] = input_list[mid]
            input_list[mid] = temp

            start += 1
            mid += 1

        elif input_list[mid] > pivot:   # current element is 2

            temp = input_list[mid]
            input_list[mid] = input_list[end]
            input_list[end] = temp

            end -= 1

        else:                           # current element is 1
            mid += 1

    print(input_list)


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
