"""
    TODO: Wrap into class

    TODO: Test Cases
        1. Empty string
        2. Single character
        3. Odd characters
"""

import sys
from heapq import heappush, heappop
from collections import defaultdict


class HuffmanNode:
    def __init__(self, weight: int, symbol=None, left=None, right=None):
        self.weight = weight
        self.symbol = symbol
        self.left = left
        self.right = right

    # Operator overloading for object comparison
    def __lt__(self, other):
        return other.weight > self.weight

    def is_leaf(self):
        return self.left is None and self.right is None


def get_frequency(data: str) -> dict:
    """
    Counts frequency of characters in a string.

    :param data: string to analyse
    :return: dict with characters as keys and their frequencies as values
    """
    chars = defaultdict()
    for char in data:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def make_heap(data: dict) -> list:
    """
    Converts a dict to a sorted list of tuples.

    :param data: dict with characters as key and their frequency as values
    :return: a list of sorted key/value pairs as tuples
    """
    return sorted([(value, key) for key, value in data.items()])


def make_nodes(nodes_list: list) -> list:
    """
    Converts a list of tuples to a list of nodes

    :param nodes_list: list of tuples
    :return: list of nodes
    """
    nodes = []
    for node in nodes_list:
        nodes.append(HuffmanNode(node[0], node[1]))
    return nodes


def build_tree(heap: list) -> list:
    """
    Builds a tree from a sorted heap by merging nodes

    :param heap: takes in a sorted list of Huffman Nodes
    :return: the tree's root node
    """
    while len(heap) > 1:
        node1 = heappop(heap)
        node2 = heappop(heap)
        merged = HuffmanNode(node1.weight + node2.weight)
        merged.left = node1
        merged.right = node2
        heappush(heap, merged)
        heap.sort()
    return heap[0]


def get_codes(root: HuffmanNode) -> dict:
    """ Uses helper function to get a dictionary of codes """
    current_code = ""
    codes = {}
    get_codes_helper(root, current_code, codes)
    return codes


def get_codes_helper(root, current_code, codes):
    """ Recursive function to determine codes of each letter """
    if root is None:
        return

    if root.symbol is not None:
        codes[root.symbol] = current_code
        return

    get_codes_helper(root.left, current_code + "0", codes)
    get_codes_helper(root.right, current_code + "1", codes)


def encode(text: str, codes: dict) -> str:
    """ Returns the encoded string as a binary sequence """
    encoded_text = ""
    for character in text:
        encoded_text += codes[character]
    return encoded_text


def get_leaf_nodes(root: HuffmanNode):
    """ Recursive In-order Tree Traversal """
    leaves = []
    if root:
        leaves = get_leaf_nodes(root.left)
        if root.is_leaf():
            leaves.append((root.weight, root.symbol))
        leaves = leaves + get_leaf_nodes(root.right)
    return leaves


def trim_tree(root: HuffmanNode):
    """ Recursive In-order Tree Traversal """
    if root:
        if not root.is_leaf():
            root.symbol = None
            root.weight = None
        get_leaf_nodes(root.left)
        get_leaf_nodes(root.right)
    return root


def decode(codes: dict, bin_data: str) -> str:
    """ Decodes a binary string into its original state """
    inv_map = {value: key for key, value in codes.items()}  # Invert the dictionary to decode the data
    current_code = ""
    decoded_text = ""
    for bit in bin_data:
        current_code += bit
        if current_code in inv_map:
            character = inv_map[current_code]
            decoded_text += character
            current_code = ""
    return decoded_text


def huffman_encoding(data: str) -> tuple:

    # 1. Get the character frequency
    frequencies = get_frequency(data)

    # 2. Make into a sorted list of tuples
    heap = make_heap(frequencies)

    # 3. Convert value to nodes
    nodes = make_nodes(heap)

    # 4. Build the tree
    root = build_tree(nodes)

    # 5. Trim tree
    root = trim_tree(root)

    # 6. Get binary codes
    codes = get_codes(root)

    # 7. Encode message
    return encode(data, codes), root


def huffman_decoding(data, tree) -> str:
    """
    Converts a binary sequence to a string.

    :param data: the binary sequence
    :param tree: the tree to reference to retrieve values
    :return: the decoded message
    """
    root = tree
    codes = get_codes(root)
    decoded_text = decode(codes, data)
    return decoded_text


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
