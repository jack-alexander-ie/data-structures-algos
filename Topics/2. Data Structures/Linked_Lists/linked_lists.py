class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def list_traverser(node):

    while node:
        print(node.value)
        node = node.next


def create_linked_list(input_list):

    head, tail = None, None

    for value in input_list:

        if head is None:

            head = Node(value)
            tail = head  # when we only have 1 node, head and tail refer to the same node

        else:

            # Because tail = head on first round, tail.next is referring to head's value,
            # and so, on the first iteration, the head value's next node is updated to the newly created node
            # From here, each new node follows the same process

            tail.next = Node(value)  # attach the new node to the `next` of tail

            # Reset the tail
            tail = tail.next  # update the tail

    return head


# head_node = create_linked_list([1, 2, 3])
# head = create_linked_list([1, 2, 3, 4, 5, 6])
# list_traverser(head)


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):

        if self.head is None:

            self.head = Node(value)

            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

        return

    def to_list(self):

        values = []
        node = self.head

        while node:
            values.append(node.value)
            node = node.next

        return values


# items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# linked_list = LinkedList()
#
# for item in items:
#     linked_list.append(item)
#
# node = linked_list.head
#
# print(linked_list.to_list())

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        # TODO: Implement this method to append to the tail of the list

        if self.head is None:

            self.head = DoubleNode(value)
            self.tail = self.head

            return

        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
double_list = DoublyLinkedList()
