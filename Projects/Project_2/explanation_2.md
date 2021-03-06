# Problem 2 - File Recursion

The only data structure used in this solution is a list which is used to collect the various filepaths for matching 
files.

A list was selected for it's simplicity:

    1. Sets - a collection of unique files is not needed
    2. Dicts - only the file names are needed, so no key/value pairs
    3. Tuples - are immutable so paths cannot be added
    4. Strings - could be used but looks untidy and does not offer versatility for potential later use
    5. Linked lists - considered to be overkill, although they'd save on the time spent doubling an array

### Time Complexity

As the directory tree has N directories and M files, every directory will be recursively searched and each file will be 
processed once when being iterated over. In this case, time complexity will be O( M + N ), or O(N).

The time complexity for this solution could be considered O(n) as the number of recursion calls made by find_files_rec()
depends on the number of sub-folders and files within a given folder.

In comparison, if it was a binary search tree a search could be completed in O(log n) time by using a divide and conquer
approach. As the given directory is not a binary tree, the best time complexity is O(n) as each and every folder and 
file has to be visited once

### Space Complexity

Similarly, the space complexity for this solution could be considered O(n) as it depends on the number of matching fies 
contained in a folder that is being searched.

## Conclusion

Time Complexity: O(n)

Space Complexity: O(n)