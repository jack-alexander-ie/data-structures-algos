def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(target, source):
    index = recursive_binary_search(target, source)

    if not index:
        return None

    while source[index] == target:
        if index == 0:
            return 0
        if source[index - 1] == target:
            index -= 1
        else:
            return index


# multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
# print(find_first(7, multiple))  # Should return 3
# print(find_first(9, multiple))  # Should return None

def contains(target, source):

    if len(source) == 0:
        return False

    center = (len(source)-1) // 2

    if source[center] == target:
        return True

    elif source[center] < target:
        return contains(target, source[center+1:])

    else:
        return contains(target, source[:center])


letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters))   # True
print(contains('b', letters))   # False
