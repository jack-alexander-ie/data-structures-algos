"""
Union and Intersection of Two Linked Lists

Fill out the union and intersection functions.

The union of two sets is the set of elements which are in the 1st list, in the 2nd list, or in both.
The intersection of two sets is the set of all objects that are members of both the sets A and B.

Take in two linked lists and return a linked list that is composed of either the union or intersection.

TODO: Test cases
TODO: Runtime analysis
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


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


def traverse_ll(head_node: Node):

    node = head_node

    while node:
        print(node.value)
        node = node.next


def create_ll_from_set(values: set) -> Node:
    linked_list = LinkedList()
    for element in values:
        linked_list.append(element)

    return linked_list.head


def union(list_1: LinkedList, list_2: LinkedList):
    union_list = set()

    node = list_1.head

    while node:
        union_list.add(node.value)
        node = node.next

    node = list_2.head

    while node:
        union_list.add(node.value)
        node = node.next

    return create_ll_from_set(union_list)


def intersection(list_1: LinkedList, list_2: LinkedList):
    ll1_as_set = set()
    ll2_as_set = set()

    node = list_1.head

    while node:
        ll1_as_set.add(node.value)
        node = node.next

    node = list_2.head

    while node:
        ll2_as_set.add(node.value)
        node = node.next

    intersection_list = (ll1_as_set ^ ll2_as_set) & ll2_as_set

    return create_ll_from_set(intersection_list)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
