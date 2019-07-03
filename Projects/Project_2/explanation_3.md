# Problem 3 - Huffman Coding

Some of the code used in this solution was referenced from the following sites:

    1. http://www.openbookproject.net/py4fun/huffman/huffman.html
    2. http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/

This solution uses a variety of data structures and methods to implement Huffman Coding, the main of which are:

    1. Strings
    2. Default dictionaries
    3. Huffman Nodes
    4. Binary Tree
    5. Priority queue (heap)

Strings are what need to be encoded and ultimately decoded at the end of the process. They're also used to store the binary sequences that represent the lossless encoded information.

Default dictionaries offer a convenient way to count the frequency of characters in a string. The O(1) lookup and update mean a string can be assessed very quickly.
If the character is not found in the dictionary, it is automatically added and does not cause a key error.

Huffman Nodes are used to generate the binary tree used to encode and decode data. Initially, they are given a symbol and the symbol's frequency as the weight.
This weight is used later by the priority queue to determine which nodes have merging priority when building the tree. 

A binary tree is at the core of the algorithm and is used to encode data and decode binary sequences. By storing symbols as leaves on a tree, a binary sequence can be obtained for each
character by traversing the tree and adding a 0 or a 1 depending if it has gone to a left or right child node. The symbols which are most frequent have the shortest path while the opposite 
is true for less frequently occurring symbols. Once the tree is complete, the symbols and weight are trimmed to save space as the tree will also need to be transported with the binary 
sequence for decoding.

A priority queue is critically important when merging nodes in the building of the binary tree. The priority queue determines which nodes to prioritise for merging and is facilitated by 
overloading the less than operator in the Huffman Node implementation.

## Time Complexity

The time complexity for implementing a huffman tree has a number if factors to consider.

### Size of the input string

As each character's frequency has to be counted, this operation has a time complexity of O(n).

### Sorting of the initial heap of nodes and the priority heap nodes

As the in-built sorted() and .sort() methods are used, sorting has a worst case time complexity of O(n log n).

### Number of symbols to build a tree with

While this is dependent on the number of different characters in the input string, and would have O(n) time complexity in the worst case, the total number of ASCII values is relatively small at 256.
While this is technically O(n), there is a cap on the the size.

This also applies for making nodes and any other list operations.

### Overall time complexity

It could be said that the overall worst case time complexity for Huffman Coding is O(n) as its time is  highly dependent on the size of the input data.

## Space Complexity

Similarly to the number of symbols to build a tree with, there's only so many nodes a tree can have when, if in the worst case, all ASCII characters are used.

That said, the space complexity of a huffman tree could be said to be O(n), as it depends on which characters appear in the inputted data.
