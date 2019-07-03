class Node:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.prev: Node = None
        self.next: Node = None


class LRUCache:
    def __init__(self, capacity):
        self.hash_table = {}
        self.capacity = capacity
        self.size = 0
        self.head: Node = None
        self.tail: Node = None
        assert self.__init_check() is True

    def get(self, key: int):
        assert type(key) is int
        assert self.__check_capacity() is True
        if self.hash_table.get(key) is None:    # Retrieve item from provided key. Return -1 if nonexistent.
            return -1
        else:
            self.__to_head(key)
            return self.head.value

    def set(self, key: int, value) -> None:
        assert type(key) is int
        assert self.__check_capacity() is True
        node = Node(key, value)                 # Set value if key not present. If at capacity, remove oldest item.
        if self.size == 0:
            self.__init_cache(key, node)        # If cache is empty, initialise it
            return
        if self.hash_table.get(key) is None:    # If key doesn't exist
            self.size += 1                      # If adding a new key, you have to increase the size
            self.hash_table[key] = node         # Add to the hash table
        else:                                   # If key exists
            self.hash_table[key].value = value  # Update the value
        self.__to_head(key)                     # Move it to the head

    def print_cache(self):
        node = self.head
        while node:
            print(node.key, node.value)
            node = node.next

    def __init_check(self) -> bool:
        if type(self.capacity) is not int:
            print('Warning: Capacity value not an integer')
            return False
        if self.capacity is 0:
            print('Warning: Initialised capacity value is 0')
        elif self.capacity < 0:
            print('Warning: Capacity value cannot be less than zero')
            return False
        return True

    def __init_cache(self, key: int, node: Node) -> None:
        self.head = node                        # Point head and tail to the same node
        self.tail = node
        self.hash_table[key] = node             # Store the memory address in the hash table
        self.size += 1                          # Increase element count

    def __check_capacity(self):
        if self.capacity is 0:
            print("Can't perform operations on 0 capacity cache")
            return False
        return True

    def __to_head(self, key: int) -> None:
        node = self.hash_table[key]
        if self.size > self.capacity:           # If it's a new node, pop off the tail
            self.__pop()
        if self.head == node:                   # Check if the node is the most recently used
            return
        if node.next:                           # If node already exists, unlink it
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        if self.tail == node:                   # Check if it's the tail so you don't get a circular linked list
            new_tail = node.prev
            new_tail.next = None
            self.tail = new_tail
        node.next = self.head                   # Add it to list head
        self.head.prev = node
        self.head = node

    def __pop(self):
        old_tail = self.tail.key                # Pop off the last element from the tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        del self.hash_table[old_tail]


# Test Case 1 - Expected output
cache = LRUCache(5)

# Set init values
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)
cache.set(5, 5)

# Get values
cache.get(1)
cache.get(4)

# Update values
cache.set(3, 7)

cache.print_cache()

"""
Expected Result:
3 7
4 4
1 1
5 5
2 2
"""

# Test Case 2 - Empty input
# cache = LRUCache(0)
# cache.set(1, 1)
# cache.get(2)

"""
Expected Result:
Warning: Initialised capacity value is 0
Can't perform operations on 0 capacity cache
AssertionError - assert self.__check_capacity() is True
"""

# Test Case 3 - Negative input
# cache = LRUCache(-2)

"""
Expected Result:
Warning: Capacity value cannot be less than or equal to zero
AssertionError - assert self.__init_check() is True
"""

# Test Case 4 - Non-integer input
# cache = LRUCache('a')
#
# cache.print_cache()

"""
Expected Result: AssertionError - type(capacity) is int
"""
