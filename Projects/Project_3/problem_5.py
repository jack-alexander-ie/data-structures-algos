from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        # Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for all complete words below this point
        pass


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add a word to the trie
        """
        current_node = self.root

        for char in word:                                    # 1. Assess each character in the inout word
            current_node = current_node.children[char]       # 2. Update the node to point it to the next node
            current_node.is_word = True                      # 3. Set the characters end_word bool to true

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        # current_node = self.root
        #
        # for char in word:
        #     if char not in current_node.children:
        #         return False
        #     current_node = current_node.children[char]
        #
        # return current_node.is_word
        pass


MyTrie = Trie()

word_list = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

print(MyTrie.root.children['a'].children['n'].children['t'].is_word)

for word in word_list:
    MyTrie.insert(word)
