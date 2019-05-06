class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def reverse_stack(stack):
    """
    Reverse in place a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """

    current_node = stack.head

    # If only one node is present
    if current_node.next is None:
        return stack

    # If two elements
    next_node = current_node.next
    current_node.next = None

    if next_node.next is None:
        next_node.next = current_node
        stack.head = next_node
        return stack

    # If several elements
    following_node = next_node.next
    next_node.next = current_node
    current_node = next_node
    next_node = following_node

    while current_node:

        if next_node.next is None:

            next_node.next = current_node
            stack.head = next_node
            return stack

        else:
            following_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = following_node