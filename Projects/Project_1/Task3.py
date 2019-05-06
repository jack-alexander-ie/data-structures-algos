"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

codes = set()

blore_outgoing_count, blore_to_blore_count = 0, 0


# For tidier parsing
def ext_between_parens(number_string):
    return number_string[number_string.find("(") + 1:number_string.find(")")]

# Worst Case Sum Expressed as: O(n) * O(n) + 3
for record in calls:

    calling, answering = record[0], record[1]

    # Check each caller
    if calling.startswith('(080)'):

        blore_outgoing_count += 1

        # Part A - Check receiver
        if answering.startswith('(0'):
            codes.add(ext_between_parens(answering))

        elif answering[0] in ['7', '8', '9']:
            codes.add(answering[:4])

        elif answering.startswith('140'):
            codes.add('140')

        # Part B - If receiver in Bangalore
        if answering.startswith('(080)'):
            blore_to_blore_count += 1

""" 
    Part A 
"""

print("The numbers called by people in Bangalore have codes:")
[print(code) for code in sorted(codes)]

"""
    Part B
"""

blore_to_blore_percent = "{0:.2f}".format(blore_to_blore_count / blore_outgoing_count * 100)
percent_str = "{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
print(percent_str.format(percentage=blore_to_blore_percent))
