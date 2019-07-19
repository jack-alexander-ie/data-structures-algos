from typing import List


def validate_value(test_value: int):
    if type(test_value) is not int or test_value < 0 or test_value > 2:
        print('Warning: Invalid value, cannot complete sorting')
        return False
    return True


def sort_012(input_list: List[int]):
    """ Sorts an array consisting of on only 0's, 1's, and 2's in a single traversal """
    next_pos_0, next_pos_2 = 0, len(input_list) - 1             # Init pointers for next positions of 0 & 2
    front_index = 0
    while front_index <= next_pos_2:

        # Test values to make sure they're valid
        assert validate_value(input_list[front_index])
        assert validate_value(input_list[next_pos_0])
        assert validate_value(input_list[next_pos_2])

        if input_list[front_index] == 0:
            input_list[front_index] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif input_list[front_index] == 2:
            input_list[front_index] = input_list[next_pos_2]
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test Cases - All should pass
# test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test Case - Invalid list values, all should fail
# test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 3])    # Expected: Warning: Invalid value, cannot complete sorting
# test_function([0, 0, -1, 2, 2, 1, 1, 1, 2, 0, 2])   # Expected: Warning: Invalid value, cannot complete sorting
# test_function([0, 0, 2, 2, 2, 1, 1, 1.0, 2, 0, 2])  # Expected: Warning: Invalid value, cannot complete sorting
# test_function([0, 0, 2, 'c', 2, 1, 1, 1, 2, 0, 2])  # Expected: Warning: Invalid value, cannot complete sorting
