from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        pass

    def insert(self, char):
        # Add a child node in this Trie
        pass

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        pass


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        pass

    def insert(self, word):
        # Add a word to the Trie
        pass

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        pass


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefix_node = MyTrie.find(prefix)
        if prefix_node:
            print('\n'.join(prefix_node.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='')
