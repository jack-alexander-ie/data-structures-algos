# Problem 3 - Rearrange Array Elements

### Time Complexity

The function `rearrange_digits` performs several operations which contribute to the overall time complexity of the 
algorithm. The first part, which tests the values in a list, ensure that only integers are in the list in `O(n)` time.

The second, and most important part, sorts the list using the `merge_sort` function. This breaks the array into `n` 
number of arrays which are then sorted one by one in `O(n log n)` time.

The third part sorts the input list in descending order so that the maximum value can be found. This is also performed 
in `O(n)` time.

Finally, the max values are found by repeating the process of popping off one integer and adding it to the first list,
then adds the next integer to the second list. This is repeated until the original list is empty. It is completed in 
`O(n)` time as it's time depends on the number of elements in the original input list.


### Space Complexity

The space complexity for this list is `O(n)` for a couple reasons. During the merge sort, the original input array is 
broken down into arrays containing one of all it's constituent parts, meaning there are at one point `O(n)` arrays.

Similarly, the strings that the integer lists are broken down into are also `O(n)` as they will hold `O(n/2)` elements 
each.

## Conclusion

Time Complexity: `O(n log n)`

Space Complexity: `O(n)`