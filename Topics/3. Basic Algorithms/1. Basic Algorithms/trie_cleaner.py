# Cleaner Trie Implementation using defautdict
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        last_index = len(word) - 1

        for index, char in enumerate(word):                  # 1. Assess each character in the input word
            current_node = current_node.children[char]       # 2. Update the node to point it to the next node
            if index is last_index:                          # 3. Set to true if last character is in the word
                current_node.is_word = True                  # 4. Flip char's is_word bool to denote complete word

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word


trie = Trie()
trie.add('cat')
trie.add('car')
trie.add('can')
trie.add('bat')
trie.add('bar')

print('Root Node:', trie.root)
print('Root Children:', trie.root.children, '\n')
print(trie.root.children['c'].children)
print(trie.root.children['c'].children['a'].children, '\n')

print(trie.exists('bat'))
print(trie.exists('ba'))
print(trie.exists('bar'))
print(trie.exists('b'))

# print(trie.exists('pen'))       # False
# print(trie.exists('garb'))      # True
# print(trie.exists('garbg'))     # False
# print(trie.exists('garbage'))   # True

# trie.add('garb')