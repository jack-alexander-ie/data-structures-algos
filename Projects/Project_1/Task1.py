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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

from itertools import chain

individual_numbers = set()

for record in chain(texts, calls):
    individual_numbers.add(record[0])
    individual_numbers.add(record[1])

record_str = "There are {count} different telephone numbers in the records."
print(record_str.format(count=len(individual_numbers)))
