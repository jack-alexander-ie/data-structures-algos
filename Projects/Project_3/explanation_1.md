# Problem 1 - Finding the Square Root of an Integer

### Time Complexity

Given a number `n`, the square root for `n` can be found using a similar process to how one finds an element in a 
sorted array with a binary search. Since `0, 1, 2...n` will always go from lowest to highest, the numbers can be 
considered the same as if they were in a sorted array, and the square root of `n` could be considered to be an element 
of that array. As a result, a similar divide and conquer approach can be utilised and a result found in `O(log n)` time.

### Space Complexity

The space complexity for this algorithm is `O(1)` as there is no growing collection of values for comparison.

## Conclusion

Time Complexity: `O(log n)`

Space Complexity: `O(1)`