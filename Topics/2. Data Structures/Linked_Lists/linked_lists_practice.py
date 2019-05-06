class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """

        if self.head is None:
            self.head = Node(value)
            return

        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        """ Append a value to the end of the list. """

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head

        # Runs until it reaches the last node
        while node.next:
            node = node.next

        # This is the next value for the last node being set
        node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """

        node = self.head

        while node:

            if node.value is value:
                return node
            else:
                node = node.next

        return None

    def remove(self, value):
        """ Remove first occurrence of value. """

        node = self.head
        prev_node = node

        while node:
            if node.value is value:

                prev_node.next = node.next
                return
            else:
                prev_node = node
                node = node.next

    def pop(self):
        """ Return the first node's value and remove it from the list. """

        if self.head is None:
            return

        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value

        node = self.head
        value = self.head.value

        next = self.head.next
        self.head = next

        return value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """

        if self.head is None:
            self.head = Node(value)
            return

        count = 0
        current_node = self.head
        prev_node = current_node

        while current_node:

            if pos is count:
                new_node = Node(value)
                new_node.next = prev_node.next
                prev_node.next = new_node
                return

            else:
                prev_node = current_node
                current_node = current_node.next
                count += 1

        if current_node.next is None and pos > count:
            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """

        if self.head is None:
            return 0

        return len(self.to_list())

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


def create_linked_from_list(values):

    linked_list = LinkedList()

    for value in values:
        linked_list.append(value)

    return linked_list


def list_traverser(node):

    while node:
        print(node.value)
        node = node.next


# items = [1]
# items = [1, 2]
# items = [1, 2, 3]
# items = [1, 2, 3, 4]
# items = [1, 2, 3, 4, 5, 6, 7]
#
# linked_list = create_linked_from_list(items)

# node = linked_list.head
# list_traverser(node)

# node = linked_list.search(4)
# print(node.value, node.next.value)

# linked_list.remove(4)
# print("Popped item:", linked_list.pop())

# linked_list.insert('a', 3)

# node = linked_list.head
# list_traverser(node)

# print('List Size:', linked_list.size())


def linked_list_reverser(list_to_reverse):

    """

    Reverse a list in place

    :param list_to_reverse:
    :return: linked list with reversed order
    """

    current_node = list_to_reverse.head

    # If only one node is present
    if current_node.next is None:
        return list_to_reverse

    # If two elements
    next_node = current_node.next
    current_node.next = None

    if next_node.next is None:
        next_node.next = current_node
        list_to_reverse.head = next_node
        return list_to_reverse

    # If several elements
    following_node = next_node.next
    next_node.next = current_node
    current_node = next_node
    next_node = following_node

    while current_node:

        if next_node.next is None:

            next_node.next = current_node
            list_to_reverse.head = next_node
            return list_to_reverse

        else:
            following_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = following_node


# linked_list_reverser(linked_list)

# items = [2, -1, 3, 0, 5]
# items = [1]
items = [1, 2, 3, 4, 5]

linked_list = create_linked_from_list(items)

list_with_loop = linked_list

# Creating a loop where the last node points back to the second node
# loop_start = linked_list.head.next

# node = linked_list.head
# while node.next:
#     node = node.next
# node.next = loop_start

# node = linked_list.head
# list_traverser(node)

def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise
    """

    # Current node
    slow_node = linked_list.head

    # Node ahead
    if slow_node.next is None:
        return False

    fast_node = slow_node.next

    while slow_node:

        if slow_node is fast_node:

            return True

        else:

            # Increment slow node by one
            slow_node = slow_node.next

            if fast_node.next is None:
                return False

            if fast_node.next.next is None:
                return False

            # Increment fast node by two
            fast_node = fast_node.next.next

    return False


print(iscircular(linked_list))
