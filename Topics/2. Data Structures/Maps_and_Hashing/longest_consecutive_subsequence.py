"""
Given list of integers that contain numbers in random order, write a program to find the longest possible sub sequence
of consecutive numbers in the array. Return this subsequence in sorted order. The solution must take O(n) time

For e.g. given the list [5, 4, 7, 10, 1, 3, 55, 2], the output should be [1, 2, 3, 4, 5]

Note- If two arrays are of equal length return the array whose index of smallest element comes first.

"""


# Brute force approach - do not use
def longest_consecutive_subsequence_bf(input_list):
    # TODO: Write longest consecutive subsequence solution
    sequence, sub_sequences = [], []

    input_list = sorted(input_list)

    # iterate over the list and store element in a suitable data structure
    for index, number in enumerate(input_list):

        print(sequence)

        if index + 1 < len(input_list):

            if input_list[index + 1] - 1 == number:
                sequence.append(number)
            else:
                sequence.append(number)
                if len(sequence) > 1:
                    sub_sequences.append(sequence)
                sequence = []

        else:
            if number - 1 == input_list[index - 1]:
                sequence.append(number)
                print(sub_sequences)
            else:
                if len(sequence) > 1:
                    sub_sequences.append(sequence)


                sequence = []

    # print(sub_sequences)

    # traverse / go over the data structure in a reasonable order to determine the solution

    longest, longest_index = 0, 0

    for index, sequence in enumerate(sub_sequences):
        if len(sequence) > longest:
            longest = len(sequence)
            longest_index = index

    return sub_sequences[longest_index]


def longest_consecutive_subsequence(input_list):
    # TODO: Write longest consecutive subsequence solution

    # iterate over the list and store element in a suitable data structure

    # traverse / go over the data structure in a reasonable order to determine the solution

    pass


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)

test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6], [8, 9, 10, 11, 12]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)
