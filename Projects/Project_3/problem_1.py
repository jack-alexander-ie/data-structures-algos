def sqrt(number):

    if number == 0 or number == 1:                      # No root, return number itself
        return number                                   # Return itself as only square

    start, end, root = 1, number, 0

    while start <= end:

        center_value = (start + end) // 2  # Center value
        center_multiplied = center_value * center_value

        if center_multiplied == number:                     # Perfect square exists, return value
            return center_value
        elif center_multiplied < number:                    # Move right
            start = center_value + 1
            root = center_value
        else:                                               # Move left
            end = center_value - 1

    return root

# Test Cases - All pass
# print("Pass" if (3 == sqrt_rec(9)) else "Fail")
# print("Pass" if (0 == sqrt_rec(0)) else "Fail")
# print("Pass" if (4 == sqrt_rec(16)) else "Fail")
# print("Pass" if (1 == sqrt_rec(1)) else "Fail")
# print("Pass" if (5 == sqrt_rec(27)) else "Fail")


# Test Case - Large numbers
# print("Pass" if (100 == sqrt_iter(10000)) else "Fail")
