""" Implementation of a Priority Queue using a Heap """


class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def __up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1)//2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break

    def __down_heapify(self):
        parent_index = 0

        while parent_index <= self.next_index:

            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2

            parent_element = self.cbt[parent_index]
            left_child_element = self.cbt[left_child_index]
            right_child_element = self.cbt[right_child_index]

            min_element = parent_element

            # Check left child exists
            if left_child_index < self.next_index:
                left_child_element = self.cbt[left_child_index]

            # Check if right child exists
            if right_child_index < self.next_index:
                right_child_element = self.cbt[right_child_index]

            # Compare with left child
            if left_child_element is not None:
                min_element = min(parent_element, left_child_element)

            # Compare with right child
            if right_child_element is not None:
                min_element = min(parent_element, right_child_element)

            # Check if parent is rightly placed
            if min_element == parent_element:
                return

            # Reset the parent's value accordingly
            if min_element == left_child_element:
                self.cbt[left_child_index] = parent_element
                self.cbt[parent_index] = min_element
                parent = left_child_index
            elif min_element == right_child_element:
                self.cbt[right_child_index] = parent_element
                self.cbt[parent_index] = min_element
                parent = right_child_index

    def __double_size(self):
        temp = self.cbt
        self.cbt = [None for _ in range(2 * len(self.cbt))]

        for index in range(self.next_index):
            self.cbt[index] = temp[index]

    def insert(self, data):

        # 1. Insert at the next available index position
        self.cbt[self.next_index] = data

        # 2. Up-heapify
        self.__up_heapify()

        # 3. Increase the index
        self.next_index += 1

        # 4. Double array and copy elements if next_index goes out
        if self.next_index >= len(self.cbt):
            self.__double_size()

    def remove(self):

        root_index = 0
        last_index = self.next_index - 1

        root_value = self.cbt[root_index]
        last_value = self.cbt[last_index]

        self.cbt[0] = last_value
        self.cbt[last_index] = None

        self.__down_heapify()

    def print(self):
        print(self.cbt)

    def size(self):
        return self.next_index


heap = Heap(10)

heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(40)
heap.insert(15)
heap.insert(60)
heap.insert(5)

heap.print()

heap.remove()

heap.print()
