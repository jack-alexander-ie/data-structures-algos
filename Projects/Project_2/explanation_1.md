# Problem 1 - LRU Cache

To solve this problem, a data structure was created using a combination of a hash table and a doubly linked list.

These structures were selected as:

    1. Doubly linked lists offer a convenient way to track least recently used items
    2. Hash tables offer O(1) time complexity for get, delete and put operations

### Why combine them?

The main drawback of using only a doubly linked list is that getting a value can only be completed in O(n) time as the list would have to be traversed until a match is found.

As for hash maps, their main drawback is that they have no order, making tracking the least recently used item very difficult.

By combining these two - the hash map for O(1) get/delete/put operations and doubly linked lists for tracking LRU values - time complexity, in the worst case scenario, is O(1).

### Space Complexity

The space complexity for this algorithm could be said to be O(n) as it entirely depends on the size of the cache that the user wants.

## Conclusion

Time Complexity: O(1)

Space Complexity: O(n)