from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        """ Adds a child node to a TrieNode """
        if len(char) > 1:
            print('Warning: Cannot add string to node - must be single character')
            return
        elif len(char) < 1:
            print('Warning: Cannot add empty character to node')
            return

        if char in self.children:               # Character is valid, check if it already exists
            print('Warning: Character already exists - please insert another')
            return
        else:
            self.children[char] = TrieNode()    # Add character if it doesn't exist

    def suffixes(self, suffix=''):
        """ Recursively collects the suffix for all complete words below a TrieNode """
        pass


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """ Adds a word to the Trie """
        current_node = self.root
        last_index = len(word) - 1
        for index, char in enumerate(word):              # 1. Assess each character in the input word
            current_node = current_node.children[char]   # 2. Update the node to point it to the next node
            if index is last_index:                      # 3. Set to true if last character is in the word
                current_node.is_word = True              # 4. Flip char's is_word bool to denote complete word

    def exists(self, word):
        """ Checks if a word exists in a Trie """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word

    def find(self, prefix):
        """ Returns a node node that represents a prefix """
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node


MyTrie = Trie()

word_list = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in word_list:
    MyTrie.insert(word)

print(MyTrie.find('ant').children)
