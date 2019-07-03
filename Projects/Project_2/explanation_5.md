# Problem 5 - Blockchain

The solution for this problem was implemented using customised nodes and linked lists.

Nodes are the most appropriate structures to use to create blocks in a chain as they must contain a variety of data and 
other data structures. They can also be hashed and linked to one another as part of a chain, two vital features of 
blockchain blocks.

Linked lists are used in blockchain technology so that a chain of accountability and security can be maintained. What 
linked lists offer over other data structures is the immutability of the block linking.

### Time Complexity

The worst case scenario for the initialisation of a blockchain and the addition of a new block to an existing chain is 
O(1).

However, the printing of the blockchain could be considered to be O(n) as it has to print the info from all blocks in 
the chain. However, for the purposes of this implementation, the print all method is not a vital feature of this 
implementation so will be ignored.

### Space Complexity

The space complexity for a block could be considered to be O(n) as it is not know what large the data is that will be 
contained.

Similarly, the space complexity of a blockchain could also be considered O(n) as the number of blocks it will contain is
not known.

## Conclusion

Time Complexity: O(1)

Space Complexity: O(n)
