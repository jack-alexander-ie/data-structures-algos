# Problem 7 - HTTPRouter using a Trie

### Time Complexity

There are two main functions in the `Router` class which add significantly to the time complexity:

    1. `add_handler`
    2. `lookup`

`add_handler` first splits the path into its constituent parts which takes `O(n)` time. It then passes the parts onto 
the Trie's insert function which cycles through each path part on `O(n)` time and traverses the trie part by part until 
an opening is found.

`lookup` also splits the path into its constituent parts in `O(n)` time and passes those parts onto the `find` function 
 of the `RouteTrie` class. The `find` function searched for each part iteratively in the Trie in `O(n)` time.

### Space Complexity

The space complexity of the `RouteTrie` class is what takes up the most space. There can be `O(n)` nodes in the trie, 
each node can have `O(n)` children and each of those nodes can also have a path part that has `O(n)` characters. This 
makes the space complexity `O(n*m)` for `nodes`, `m` which is children + path size.

## Conclusion

Time Complexity: `O(n)`

Space Complexity: `O(n*m)`