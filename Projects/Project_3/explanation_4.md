# Problem 4 - Dutch National Flag Problem

Note: This algorithms was referenced from the one provided by Udacity during coverage of this particular problem.

### Time Complexity

The time complexity for this algorithm is `O(n)` as the it will have to traverse the array once to complete its sorting.

Three pointers are maintained to track the location of certain variables:

    1. `next_pos_0` : The next position to place a zero
    2. `next_pos_2` : The next position to place a two
    3. `front_index` : The front of the list

For each value in the list, it tests to see if:

    1. The first value is 0
    2. The first value is 2
    3. The first value is 1

Depending on which value is found, the algorithm will place the value in the correct place using its relevant pointer.

### Space Complexity

It's space complexity is also `O(n)` as the number of elements in the input list is not fixed.

## Conclusion

Time Complexity: `O(n)`

Space Complexity: `O(n)`
