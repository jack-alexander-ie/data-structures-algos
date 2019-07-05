def sqrt(number, comparator=-1, prev_mult=0):

    # Test block for initial call
    if comparator == -1:
        comparator = number

    if comparator == 0 or comparator == 1:              # No root, return number itself
        return number                                   # Return itself as only square

    center_value = (comparator - 1) // 2                # Center value
    center_multiplied = center_value * center_value

    if center_multiplied == number:                     # Perfect square exists, return value
        return center_value
    elif center_multiplied < number:                    # Move right

        prev_square = prev_mult * prev_mult             # Get square of previous multiplier
        if prev_square > number:                        # If previous square > target..
            return center_value                         # ..return floored value

        return sqrt(number, comparator + 1, center_value)
    else:                                               # Move left
        return sqrt(number, comparator - 1, center_value)


# Test Cases
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
