# Problem 5 - Autocomplete with Tries

### Time Complexity

There are several functions which have a varying effect of the time complexity of the algorithm.

Inserting a word into the Trie take `O(n)` time as it has to cycle through `O(n)` characters in the word and add each 
accordingly.

Finding a word in the Trie takes `O(n)` time as, similarly to insertion, it has to cycle through each character in the 
word.

Collecting the suffixes is completed in `O(n*m)` time as it has to search recursively for each word end in each nodes 
children.

### Space Complexity

The space complexity of the Trie is `O(n*m)` where `n` is the number of characters in the alphabet and `m` is the number
 of children it has.

## Conclusion

Time Complexity: `O(n*m)` (Worst case for finding suffixes)

Space Complexity: `O(n*m)`
