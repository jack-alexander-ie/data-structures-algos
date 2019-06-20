class Node:
    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.prev: Node = None
        self.next: Node = None


class LRUCache:

    def __init__(self, capacity):
        # Initialize class variables
        self.hash_table = {}
        self.capacity = capacity
        self.size = 0
        self.head: Node = None
        self.tail: Node = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.hash_table.get(key) is None:
            return -1
        else:
            self.__to_head(key)
            return self.head.value

    def set(self, key, value) -> None:
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        node = Node(key, value)

        # If cache is empty, initialise it
        if self.size == 0:
            self.__init_cache(key, node)
            return

        # If key doesn't exist
        if self.hash_table.get(key) is None:
            # If adding a new key, you have to increase the size
            self.size += 1
            # Add to the hash table
            self.hash_table[key] = node
        # If key exists
        else:
            # Update the value
            self.hash_table[key].value = value

        # Move it to the head
        self.__to_head(key)

    def __init_cache(self, key, node) -> None:
        # Point head and tail to the same node
        self.head = node
        self.tail = node

        # Store the memory address in the has table
        self.hash_table[key] = node

        # Link the head and tail nodes
        self.head.next = self.tail
        self.tail.prev = self.head

        # Increase element count
        self.size += 1

    def __to_head(self, key) -> None:

        node = self.hash_table[key]

        # If it's a new node, pop off the tail
        if self.size > self.capacity:
            self.__pop()

        # Check if the node is the most recently used
        if self.head == node:
            return

        # If node already exists, unlink it
        if node.next:
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

        # Check if it's the tail so you don't get a circular linked list
        if self.tail == node:
            new_tail = node.prev
            new_tail.next = None
            self.tail = new_tail

        # Add it to list head
        node.next = self.head
        self.head.prev = node
        self.head = node

        # Update the hash table
        # self.hash_table[key] = node

    def __pop(self) -> Node:
        # Pop off the last element from the tail
        old_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        del self.hash_table[old_tail.key]
        return old_tail


def print_vals(node):
    while node:
        print('value:', node.value)
        node = node.next
    # print()


def print_dict(items):
    for key, value in items:
        print('Key:', key)


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

our_cache.get(1)

our_cache.set(6, 6)

# print_vals(our_cache.head)
# print_dict(our_cache.hash_table.items())
