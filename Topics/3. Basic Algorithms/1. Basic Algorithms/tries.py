basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie

    for char in word:
        if char not in current_node:
            return False

        current_node = current_node[char]

    return current_node['word_end']


# Test words - is_word()
# test_words = ['ap', 'add']
# for word in test_words:
#     if is_word(word):
#         print('"{}" is a word.'.format(word))
#     else:
#         print('"{}" is not a word.'.format(word))


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:                                   # 1. Assess each character in the inout word
            if char not in current_node.children:           # 2a. If the character is not an existing character
                current_node.children[char] = TrieNode()    # 2b. Add it to the list of acceptable characters
            current_node = current_node.children[char]      # 3. Update the node to point it to the next node

        current_node.is_word = True                         # Set the characters end_word bool to true

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


# trie = Trie()
#
# trie.add('garbage')
# trie.add('garb')
#
# print(trie.exists('pen'))       # False
# print(trie.exists('garb'))      # True
# print(trie.exists('garbg'))     # False
# print(trie.exists('garbage'))   # True


# Cleaner Trie Implementation using defautdict
from collections import defaultdict


class TrieNodeCleaner:
    def __init__(self):
        self.children = defaultdict(TrieNodeCleaner)
        self.is_word = False


class TrieCleaner:
    def __init__(self):
        self.root = TrieNodeCleaner()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:                                    # 1. Assess each character in the inout word
            current_node = current_node.children[char]       # 2. Update the node to point it to the next node
            current_node.is_word = True                      # 3. Set the characters end_word bool to true

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

trie.add('garbage')
trie.add('garb')

print(trie.exists('pen'))       # False
print(trie.exists('garb'))      # True
print(trie.exists('garbg'))     # False
print(trie.exists('garbage'))   # True
