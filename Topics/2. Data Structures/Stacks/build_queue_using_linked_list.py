class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):

        node = Node(value)
        self.num_elements += 1

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def dequeue(self):

        if self.is_empty():
            return

        value = self.head.value
        next = self.head.next

        self.head = next
        self.num_elements -= 1

        return value

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def iterate(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

# q.iterate()

# print(q.head.value)
# print(q.tail.value)
# print(q.is_empty())
# print(q.size())

print("Dequeued item:", q.dequeue(), '\n')

q.iterate()
