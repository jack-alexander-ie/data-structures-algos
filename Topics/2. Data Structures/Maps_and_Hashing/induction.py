"""

A child is running up a staircase with and can hop either 1 step, 2 steps or 3 steps at a time. If the staircase has n
steps, write a function to count the number of possible ways in which child can run up the stairs.

e.g.    n == 1 then answer = 1
        n == 3 then answer = 4
        n == 5 then answer = 13

"""

from functools import lru_cache

"""

Definition: f(n) = f(n-1) + f(n-2) + f(n-3)

The number of f(n) recursive functions depends on the number of steps allowed to take each time.

"""

# Naive approach doesn't use caching
@lru_cache(maxsize=1000)
def staircase_lru(n):
    # Base Case - minimum steps possible and number of ways the child can climb them
    if n == 1:
        return 1
    # Inductive Hypothesis - ways to climb rest of the steps
    elif n == 2:
        return 2
    # Inductive Step - use Inductive Hypothesis to formulate a solution
    elif n == 3:
        return 4

    return staircase_lru(n - 1) + staircase_lru(n - 2) + staircase_lru(n - 3)


# print(staircase_lru(100))


def staircase(n):
    num_dict = dict({})
    return staircase_faster(n, num_dict)


def staircase_faster(n, num_dict):
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:

        # 1. Check if value stored in cache
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]
        # 2. If not, make a recursive call to calculate it
        else:
            first_output = staircase_faster(n - 1, num_dict)

        # Repeat aforementioned process..
        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)

        # Repeat aforementioned process...
        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)

        # Final output
        output = first_output + second_output + third_output

    num_dict[n] = output
    return output


print(staircase(100))
