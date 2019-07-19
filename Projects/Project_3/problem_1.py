def sqrt(number: int) -> int:
    if type(number) is not int:
        print('Warning: Input can only be an integer')
        return 0
    if number < 2:                              # No root
        return number                           # Return itself
    low, high = 1, number//2                    # Square root cannot be more than num/2
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


# Test Cases - All should pass
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Test Case - Large numbers should pass too
print("Pass" if (100 == sqrt(10000)) else "Fail")

# Test Case - Input not an integer
sqrt('a')   # Output should be 'Warning: Input can only be an integer'
