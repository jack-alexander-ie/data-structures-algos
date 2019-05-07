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


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def iterate(self):

        node = self.head

        while node:
            print(node.value)
            node = node.next


def reverse_queue(queue):
    """
    Reverse the input queue

    Args:
       queue(queue),str2(string): Queue to be reversed
    Returns:
       queue: Reversed queue
    """

    head = queue.head
    current_node = queue.head

    # If only one node is present
    if current_node.next is None:
        return queue

    # If two elements
    next_node = current_node.next
    current_node.next = None

    if next_node.next is None:
        next_node.next = current_node
        queue.tail = current_node
        queue.head = next_node
        return queue

    # If several elements
    following_node = next_node.next
    next_node.next = current_node
    current_node = next_node
    next_node = following_node

    while current_node:

        if next_node.next is None:

            next_node.next = current_node
            queue.tail = head
            queue.head = next_node
            return queue

        else:
            following_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = following_node


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

reverse_queue(q)

print(q.head.data)
print(q.tail.data)
