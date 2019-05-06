"""

    Generators let you go off and do other things by pausing an active process.

    Similar to a function except instead of returning a value and exiting a process,
    a generator will pause the process, saving its state for the next time.

    Biggest difference between a function and a generator from a code perspective is:

    return vs. yield

    Generators are used when dealing with a large collection of data that you don't
    want to store in memory all at once. Also useful for dealing with very large or
    infinite series.

"""


# Definition of the generator to produce even numbers.
def all_even():
    n = 0

    while True:
        yield n

        n += 2


# my_gen = all_even()

# Generate the first 5 even numbers.
# for i in range(5):
#     print(next(my_gen))

# Now go and do some other processing.
# do_something = 4
# do_something += 3
# print('BREAKER', do_something)

# Now go back to generating more even numbers.
# for i in range(20):
#     print(next(my_gen))

''' 
    Task 

    In the following exercise, you will create a generator 
    fact_gen() that generates factorials. For a number n, n 
    factorial is denoted by n!, and it is the product of all 
    positive integers less than or equal to n. 
    
    e.g. 5! = 5*4!*3!*2!*1
    
    In this exercise, you will define prod(a, b) which returns 
    the product of numbers a and b. You will also define fact_gen() 
    which yields the next factorial number.

'''


def prod(a, b):
    output = a * b
    return output


def fact_gen():
    i = 1
    n = i

    while True:
        output = prod(n, i)

        i += 1
        n = output

        yield output


# Test block
my_gen = fact_gen()

num = 5

# for i in range(num):
#     print(next(my_gen))

''' 
    Task 

    You will write a function that checks sudoku squares for correctness.
    
    Define a procedure, check_sudoku, that takes as input a square list of lists representing an 
    n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square 
    and returns the boolean False otherwise.

    A valid sudoku square satisfies these two properties:
    
        1. Each column of the square contains each of the whole numbers from 1 to n exactly once.
        
        2. Each row of the square contains each of the whole numbers from 1 to n exactly once.
    
    You may assume that the input is square and contains at least one row and column.

'''

correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


def check_sudoku1(square_list):

    value_range = len(square_list[0])

    # Check squares in a row
    for row in square_list:

        values = []

        for value in row:

            if type(value) is int and value <= len(row) and value not in values:

                values.append(value)
            else:
                return False

    # Check squares in a single column
    # For value in each row at the nth position
    for value in range(value_range):

        print('Checking column value at position', value)

        # Values to compare against / values to pop off
        check_list = list(range(1, len(square_list[0]) + 1))

        print('List to Compare Against:', check_list)

        for row in square_list:

            print('Comparison Value:', row[value])

            if row[value] not in check_list:

                print('No Match:', row[value])
                return False

            check_list.remove(row[value])

        print()

    return True


# print()
# print(check_sudoku1(correct), '\n')
# >>> True

# print(check_sudoku1(incorrect), '\n')
# >>> False

# print(check_sudoku1(incorrect2), '\n')
# >>> False

# print(check_sudoku1(incorrect3), '\n')
# >>> False

# print(check_sudoku1(incorrect4), '\n')
# >>> False

# print(check_sudoku1(incorrect5), '\n')
# >>> False


def sudoku_check(sudoku_list):

    row_length = len(sudoku_list[0])
    list_of_values = list(range(1, row_length + 1))

    for row in sudoku_list:

        # check_list = list(range(1, row_length + 1))
        check_list = list(list_of_values)

        for value in row:

            if value in check_list:

                check_list.remove(value)

            else:

                return False

    for index in range(row_length):

        # check_list = list(range(1, row_length + 1))
        check_list = list(list_of_values)

        for row in sudoku_list:

            if row[index] in check_list:

                check_list.remove(row[index])

            else:

                return False

    return True


# print()
print(sudoku_check(correct), '\n')
# >>> True

print(sudoku_check(incorrect), '\n')
# >>> False

print(sudoku_check(incorrect2), '\n')
# >>> False

print(sudoku_check(incorrect3), '\n')
# >>> False

print(sudoku_check(incorrect4), '\n')
# >>> False

print(sudoku_check(incorrect5), '\n')
# >>> False
