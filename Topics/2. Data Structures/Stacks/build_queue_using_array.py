class Queue:

    def __init__(self, init_size=10):
        self.arr = [0 for _ in range(init_size)]
        # Stores next index slot to be filled
        self.next_index = 0

        # -1 because when you increment, index then starts at 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):

        if self.queue_size == len(self.arr):
            self._handle_capacity_full()

        self.arr[self.next_index] = value
        self.queue_size += 1

        # Refer back to the array size as it will change
        self.next_index = (self.next_index + 1) % len(self.arr)

        # Only needs to be incremented once
        if self.front_index == -1:
            self.front_index = 0

    def dequeue(self):

        # Reset queue if empty
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None

        value = self.arr[self.front_index]

        # Shift head so it refers to next_index
        self.front_index = (self.front_index + 1) % len(self.arr)

        self.queue_size -= 1
        return value

    def _handle_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(self.queue_size*2)]
        for index, value in enumerate(old_arr):
            self.arr[index] = value

        # Set new index point, based on old array's length
        self.next_index = len(old_arr) % len(self.arr)

    def front(self):
        if not self.is_empty:
            return self.arr[self.front_index]

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size is 0


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)

# print(q.queue_size)

print(q.arr)
