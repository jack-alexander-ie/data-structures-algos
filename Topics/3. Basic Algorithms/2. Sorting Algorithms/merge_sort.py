def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2

    # Split the array
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):  # Move through the lists until we have exhausted one

        if left[left_index] > right[right_index]:   # If left's item larger, append right's item & increment index
            merged.append(right[right_index])
            right_index += 1
        else:                                       # Otherwise, append left's item and increment
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop, we know at least one is empty, and the remaining:
    #   a) are already sorted
    #   b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    return merged   # return the ordered, merged list


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))

test_list_4 = [3, 2, 5, 3, 1, 5, 1, 3, 6, 1]
print('{} to {}'.format(test_list_4, mergesort(test_list_4)))
