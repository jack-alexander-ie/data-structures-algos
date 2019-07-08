def heapsort(arr):
    heapify(arr, len(arr), 0)


def heapify():
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Convert an array (in place) into a maxheap, a complete binary tree with the largest values at the top

    TODO: Steps
        1. Convert array to maxheap
        2. Swap the top element with the last array element
        3. Repeat with arr[:len(arr)-1]
    """