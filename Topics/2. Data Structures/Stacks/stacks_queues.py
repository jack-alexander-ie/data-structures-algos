# class Stack:
#
#     def __init__(self):
#         self.array = []
#
#     def push(self, value):
#         self.array.append(value)
#
#     def pop(self):
#         value = self.array[len(self.array) - 1]
#         self.array.remove(value)
#         return value
#
#     def size(self):
#         return len(self.array)
#
#     def top(self):
#         return self.array[len(self.array) - 1]
#
#     def is_empty(self):
#         if self.size() > 0:
#             return False
#
#         return True


class Stack:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):

        if self.next_index >= len(self.arr):
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def pop(self):

        # Empty check
        if self.is_empty():
            self.next_index = 0
            return None

        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):

        old_arr = [item for item in self.arr]
        self.arr = [0 for _ in range(self.num_elements*2)]

        for index, value in enumerate(old_arr):
            self.arr[index] = value

items = Stack()

items.push(1)
items.push(2)
items.push(3)
items.push(4)
items.push(5)

print(items.arr)

print('Popped Item:', items.pop())

print(items.arr)
