def is_palindrome(input):

    # Base Case - if down to a single letter or none at all
    if len(input) <= 1:
        return True
    else:
        first, last = input[0], input[-1]

        # Recursive Case
        # First and last letters match, and True from base case
        return (first == last) and is_palindrome(input[1:-1])


print(is_palindrome('cchahccc'))
