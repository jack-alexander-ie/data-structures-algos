def sqrt(number):

    if number < 2:                              # No root, return number itself
        return number                           # Return itself as only square

    low, high = 1, number//2                    # Square root cannot be more than number/2

    result = 0

    while low <= high:

        mid_value = (low + high) // 2           # Center value
        mid_squared = mid_value * mid_value

        if mid_squared == number:               # Perfect square exists, return value
            return mid_value
        elif mid_squared < number:              # Move right
            low = mid_value + 1
            result = mid_value
        else:                                   # Move left
            high = mid_value - 1

    return result

# Test Cases - All pass
# print("Pass" if (3 == sqrt_rec(9)) else "Fail")
# print("Pass" if (0 == sqrt_rec(0)) else "Fail")
# print("Pass" if (4 == sqrt_rec(16)) else "Fail")
# print("Pass" if (1 == sqrt_rec(1)) else "Fail")
# print("Pass" if (5 == sqrt_rec(27)) else "Fail")

# Test Case - Large numbers
# print("Pass" if (100 == sqrt(10000)) else "Fail")
