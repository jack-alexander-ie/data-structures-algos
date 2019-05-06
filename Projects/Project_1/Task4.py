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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_telemarketers = set()

# Add all outgoing numbers to the list
for record in calls:
    possible_telemarketers.add(record[0])

# Compare receiving numbers against known outgoing numbers
for record in calls:
    if record[1] in possible_telemarketers:
        possible_telemarketers.remove(record[1])

# Check text records against known possible telemarketers
for record in texts:

    outgoing, receiving = record[0], record[1]

    if outgoing in possible_telemarketers:
        possible_telemarketers.remove(outgoing)

    if receiving in possible_telemarketers:
        possible_telemarketers.remove(receiving)

print("These numbers could be telemarketers: ")
[print(number) for number in sorted(possible_telemarketers)]
