# Problem 2 - Search in a Rotated Sorted Array

### Time Complexity

Two binary searches are employed in this algorithm - one to find the pivot index of the rotated array, if it is a 
rotated array being searched, and another to search recursively for the target number, if it exists.

The time complexity for this implementation is `O(log n)` due to the two search operations that are performed.

### Space Complexity

The space complexity for this problem is `O(n` as the two arrays (`arr_one` and `arr_two`) that the original array is 
split into is `O(n)`.

## Conclusion

Time Complexity: `O(log n)`

Space Complexity: `O(n)`