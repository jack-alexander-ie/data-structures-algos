""" Rearrange Array Elements """


def mergesort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergesort(L)  # Sorting the first half
        mergesort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # 1. Sort the input list - O(n log n)
    mergesort(input_list)

    # 2. Sort list into descending order - O(n)
    reverse_list(input_list)

    # 3. Return max pair - O(n)
    return find_max_pair(input_list)


def reverse_list(list_of_nums):
    """ Reversal in-place of elements """
    for i in range(len(list_of_nums)):
        number = list_of_nums.pop()
        list_of_nums.insert(i, number)


def find_max_pair(input_list):

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


# test_function([[1, 2, 3, 4, 5], [542, 31]])
# test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
