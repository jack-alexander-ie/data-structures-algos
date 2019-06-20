"""
Given an input_list and a target, return the indices of pair of integers in the list that sum to the target.

The best solution takes O(n) time. You can assume that the list does not have any duplicates.

e.g. input_list = [1, 5, 9, 7] and target = 8, the answer would be [0, 3]
"""


def pair_sum_to_zero(input_list, target):
    index_dict = dict()
    for index, element in enumerate(input_list):

        print(target - element)
        print(index_dict, '\n')

        if target - element in index_dict:
            return [index_dict[target - element], index]
        index_dict[element] = index


print(pair_sum_to_zero([1, 6, 9, 7], 8))
