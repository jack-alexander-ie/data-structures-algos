"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """TODO: Input a string that's stored in the table."""
        hash_value = self.calculate_hash_value(string)

        if self.table[hash_value] is None:
            self.table[hash_value] = [string]
        else:
            self.table[hash_value].append(string)

    def lookup(self, string):
        """TODO: Return the hash value if the string is already in the table. Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)

        if self.table[hash_value] is not None:
            return hash_value
        else:
            return -1

    def calculate_hash_value(self, string) -> int:
        """TODO: Helper function to calculate a hash value from a string."""

        key = str(string[:2])
        key_sum = []
        for character in key:
            key_sum.append(ord(character))

        key_sum[0] = key_sum[0] * 100
        hash_value = sum(key_sum)
        return hash_value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))

