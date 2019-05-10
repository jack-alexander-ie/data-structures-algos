from copy import deepcopy


def permute(l):

    # Stores permutations after recursive call
    perm = []

    # Base Case - return an empty list
    if len(l) == 0:

        print()
        print('Base reached, returning back up...\n')
        print('------', '\n')
        perm.append([])

    else:
        # First used for recursive insertion
        first, rest = l[0], slice(1, None)

        sub_perms = permute(l[rest])

        # For loop is run len(original_input) times as each recursive call has to finish out the instructions
        print('Completing recursive call', str(len(l)) + '...\n')

        # List of sub-permutations is [[], [3], [2, 3], [3, 2]] after the recursive calls
        for permutation in sub_perms:

            """
            Insert operation important here.

            In the case of [1, 2, 3]:

                1. Creates permutations of [] first -> inserts only one value [3]
                    => Result: [3]
                2. Creates permutations of [3] by inserting 2 to front, increasing the index, then 2 at the end 
                    => Result: [[2, 3], [3, 2]]
                3. Creates permutations of [2, 3] by inserting 1 to front, 1 to middle, 1 to end 
                    => [[1, 2, 3], [2, 1, 3], [2, 3, 1]]
                4. Creates permutations of [3, 2] by inserting 1 to front, 1 to middle, 1 to end 
                    => [[1, 2, 3], [2, 1, 3], [2, 3, 1]]
            """

            print('Current Permutation:', permutation)

            # Use j for insert index - counts to len of permutation
            # Iterate over the permutation itself
            for index in range(len(permutation) + 1):

                # Create a deep copy as you don't want to change the original permutation value
                deep_perm = deepcopy(permutation)

                # Uncomment preceding deep_perm and see what happens here
                # deep_perm = permutation

                print('Current Insertion Value:', first)

                # Insert first character at index j -
                # first refers back to character from recursion stored previously
                print("\n \t Inserting", first, "into permutation", deep_perm, 'at index', index)
                deep_perm.insert(index, first)

                # Append amended permutation to the list
                perm.append(deep_perm)

                print()
                print('Appended permutation:', deep_perm, '\n')

            print()
            print('Current Permutations List:', perm, '\n')

            print('------', '\n')

    return perm


# print('Final list of permutations:', permute([1, 2, 3]), '\n')


def permute_test(l):

    perms = []

    if len(l) == 0:
        perms.append([])

    else:

        first, rest = l[0], slice(1, None)

        sub_permutations = permute_test(l[rest])

        for permutation in sub_permutations:

            # Iterate over the permutation itself
            for index in range(len(permutation) + 1):

                deep_perm = deepcopy(permutation)

                deep_perm.insert(index, first)

                perms.append(deep_perm)

    return perms


print('Final list of permutations:', permute_test([1, 2, 3]), '\n')
