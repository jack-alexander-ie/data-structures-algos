class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):                # Overloaded so raw node values can be compared
        return self.value == other.value

    def __hash__(self):                     # Overloaded so nodes can be hashed for use in set
        return hash(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def create_ll_from_set(values: set) -> LinkedList:
    linked_list = LinkedList()
    for element in values:
        linked_list.append(element)
    return linked_list


def collect_ll_vals(head_node) -> set:
    values = set()
    node = head_node
    while node:
        values.add(node)
        node = node.next
    return values


def collect_from_lists(list_1: LinkedList, list_2: LinkedList):
    if type(list_1) != LinkedList or type(list_2) != LinkedList:
        print('One or more input lists is not a linked list, exiting...')
        exit()
    if list_1.head is None or list_2.head is None:
        print('Warning: One or more lists contain no values')
    list_1_vals, list_2_vals = collect_ll_vals(list_1.head), collect_ll_vals(list_2.head)
    return list_1_vals, list_2_vals


def union(list_1: LinkedList, list_2: LinkedList) -> LinkedList:
    vals = collect_from_lists(list_1, list_2)
    union_list = vals[0].union(vals[1])
    return create_ll_from_set(union_list)


def intersection(list_1: LinkedList, list_2: LinkedList) -> LinkedList:
    vals = collect_from_lists(list_1, list_2)
    intersection_list = vals[0].intersection(vals[1])
    return create_ll_from_set(intersection_list)


# Test Case 1 - Expected
element_1, element_2 = {3, 2, 4, 35, 6, 65, 6, 4, 3, 21}, {6, 32, 4, 9, 6, 1, 11, 21, 1}
linked_list_1, linked_list_2 = create_ll_from_set(element_1), create_ll_from_set(element_2)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

"""
Expected Output:

32 -> 65 -> 2 -> 3 -> 35 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
4 -> 21 -> 6 ->
"""

# Test Case 2 - Empty set(s)
# element_1, element_2 = set(), set()
# linked_list_1, linked_list_2 = create_ll_from_set(element_1), create_ll_from_set(element_2)
# print(union(linked_list_1, linked_list_2))
# print(intersection(linked_list_1, linked_list_2))

"""
Expected Output:

Warning: One or more lists contain no values

Warning: One or more lists contain no values

"""

# Test Case 3 - Incorrect data types
# element_1, element_2 = {3, 2, 4, 35, 6, 65, 6, 4, 3, 21}, dict()
# linked_list_1, linked_list_2 = create_ll_from_set(element_1), create_ll_from_set(element_2)
# print(union(linked_list_1, linked_list_2))
# print(intersection(linked_list_1, linked_list_2))
"""
Expected Output: One or more input lists is not a linked list, exiting...
"""