class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)
        return bucket_index

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            # Ord function returns AASCII value of character - Multiply AASCII value * coefficient
            hash_code += ord(character) * current_coefficient

            # Compress the resulting number by dividing by len of the bucket array
            hash_code = hash_code % num_buckets  # compress hash_code

            # Multiply current coefficient by itself
            current_coefficient *= self.p

            # Compress the coefficient
            current_coefficient = current_coefficient % num_buckets  # compress coefficient

        """
                Because of how modulo operator works, instead of creating a new function, 
                we can write the logic for compression function in our get_hash_code() function itself.
        """
        return hash_code % num_buckets  # one last compression before returning

    def size(self):
        return self.num_entries


# hash_map = HashMap()

# Uses Hash Map object to create and retrieve hashed value
# bucket_index = hash_map.get_bucket_index("abcd")
# print(bucket_index)
#
# bucket_index = hash_map.get_bucket_index("bcda")
# print(bucket_index)


hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))
