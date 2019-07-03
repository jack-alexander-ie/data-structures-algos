# Problem 2 - File Recursion

The only data structure used in this solution is a list which is used to collect the various filepaths for matching files.

A list was selected for it's simplicity:

    1. Sets - a list of unique files is not needed
    2. Dicts - only the file names are needed, so no key/value pairs
    3. Tuples - are immutable so paths cannot be added
    4. Strings - could be used but looks untidy and does not offer versatility for potential later use
    5. Linked lists - could be considered to be overkill, even though they'd save on the computational time spent doubling an array

### Time Complexity

The time complexity for this solution could be considered O(n) as it depends on the number of matching fies contained in a folder.

### Space Complexity

Similarly, the space complexity for this solution could be considered O(n) as it depends on the number of matching fies contained in a folder.

## Conclusion

Time Complexity: O(n)

Space Complexity: O(n)