from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char: str) -> None:
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

    def suffixes(self, suffix: str = '') -> list:
        """ Recursively collects all the suffixes for a given node """

        suffixes = ['test']

        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """ Adds a word to the Trie """
        current_node = self.root
        last_index = len(word) - 1
        for index, char in enumerate(word):              # 1. Assess each character in the input word
            current_node = current_node.children[char]   # 2. Update the node to point it to the next node
            if index is last_index:                      # 3. Set to true if last character is in the word
                current_node.is_word = True              # 4. Flip char's is_word bool to denote complete word

    def exists(self, word: str) -> bool:
        """ Checks if a word exists in a Trie """
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word

    def find(self, prefix: str) -> TrieNode:
        """ Returns a node node that represents a prefix """
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                print('Warning: Prefix does not exists in the Trie')
                return
            current_node = current_node.children[char]
        return current_node


MyTrie = Trie()

word_list = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", "factorial",
    "trie", "trigger", "trigonometry", "tripod"
]

for word in word_list:
    MyTrie.insert(word)

parent_node = MyTrie.find('f')
print(parent_node.children)
suffixes = parent_node.suffixes()

print(suffixes)
