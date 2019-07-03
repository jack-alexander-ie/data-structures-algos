# Problem 4 - Active Directory

This implementation of active directory uses very few data structures. The following are used:

    1. Strings
    2. Lists
    3. Group (custom data structure)

Strings are used to stored the name of groups, their children and individual users.

Lists are used to store instances of groups and the name of their users.

The group class itself is implemented using a combination of strings and lists to store group and user information.

The is_user_in_group() method was implemented in a recursive manner as this was deemed to be for most effective way to 
search through all the group and their subgroups, and is a similar implementation fto the recursive search problem.

### Time Complexity

The time complexity of the is_user_in_group() method is O(n) and it has to search through an unknown number of groups 
and subgroups.

The overall time complexity could be considered to be O(n)

### Space Complexity

With regards to space complexity, the implementation of the is_user_in_group() method could be considered to be O(1) 
as all that is returned is a single boolean value.

If it is being assessed, the number of groups and their users has a space complexity of O(n) as any number of groups and users can be added.

## Conclusion

Time Complexity: O(n)

Space Complexity: O(1) (but O(n) if user generation is being assessed)
