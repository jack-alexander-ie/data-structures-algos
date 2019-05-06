class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def traverse(self):
        node = self.head

        while node:

            print(node.value)

            if node.next is None:
                return
            else:
                node = node.next

    # These push and pop implementations allow pushing and popping in O(1) time.
    def push(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.num_elements += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.num_elements += 1

    def pop(self):

        if self.head is None:
            return None

        value = self.head.value
        next_node = self.head.next
        self.head = next_node
        self.num_elements -= 1

        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements is 0


# items = Stack()
#
# items.push(1)
# items.push(2)
# items.push(3)
# items.push(4)

# items.traverse()
#
# print('value:', items.pop())
#
# items.traverse()
#
# print('size', items.size())
# print(items.is_empty())

def oddNumbers(l, r):

    odd_numbers = []

    for number in range(l, r + 1):

        if number % 2 != 0:
            odd_numbers.append(number)

    return odd_numbers


print(oddNumbers(2, 9))
