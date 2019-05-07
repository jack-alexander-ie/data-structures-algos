class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.instorage = Stack()
        self.outstorage = Stack()

    def size(self):
        return self.outstorage.size() + self.instorage.size()

    def enqueue(self, item):
        self.instorage.push(item)

    def dequeue(self):
        # If out stack is empty
        if not self.outstorage.items:

            # While in stack has items
            while self.instorage.items:

                # Fill the out stack with those items
                self.outstorage.push(self.instorage.pop())

        # Otherwise, just return the last from the previously filled out stack
        return self.outstorage.pop()


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print('Dequeued item:', q.dequeue())

q.enqueue(6)
q.enqueue(7)
q.enqueue(8)

# Won't print output until existing out stack is emptied
print('Dequeued item:', q.dequeue())
