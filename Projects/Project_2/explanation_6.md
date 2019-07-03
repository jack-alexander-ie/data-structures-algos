# Problem 6 - Union and Intersection

The set() data structure was chosen to solve the union and intersection problems as it allows for O(1) lookup. While a 
dictionary could also be used, it would not be as tidy a solution.

### Time Complexity

Union, in the worst case, is completed in O(n) time. There a several steps which make this the case:

    1. The values have to be collected from the nodes first for creating sets
    2. The number of lookup operations the set performs depends on the number of values to look up
    3. Generating the linked lists for the new sets

Intersection, in the worst case, is also completed in O(n) time and is so for the same very same reasons.

### Space Complexity

Both solutions have a space complexity of O(n). The size of the sets and the linked lists depend entirely on the size of
the input sets.

## Conclusion

Time Complexity: O(n) for both functions

Space Complexity: O(n) for both functions
