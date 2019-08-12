import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value_jack(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """

    knapsack_table = [0 for _ in range(knapsack_max_weight + 1)]

    # Last tested item and max value
    last_weight, last_value, prev_index = 0, 0, 0

    while len(items) > 0:

        item = items.pop()
        item_weight, item_value = item[0], item[1]
        last_weight, last_value = item_weight, item_value

        print(knapsack_table, '\n', item_weight, item_value, '\n')

        start_index = item_weight + 1

        # Update the values
        for value in knapsack_table[start_index:]:
            if item_value > value:
                knapsack_table[start_index] = item_value
                # TODO: Inefficient as updated n times
                prev_index = item_weight + 1
            start_index += 1

    # Grab value from its starting point
    max_value = knapsack_table[prev_index]

    for index, value in enumerate(knapsack_table):

        # Grab the previous value and add it to the current nth position
        comparator = value + last_value

        print('Max Value', max_value, '\t Comparator:', comparator)

        if comparator > max_value:
            max_value = comparator
            knapsack_table[index] = max_value

            print(prev_index, len(knapsack_table))

        prev_index += 1

    print()
    print(knapsack_table)

    return knapsack_table[-1]


# Correct output is 14
# print(max_value_jack(15, [Item(10, 7), Item(9, 8), Item(5, 6)]))

def max_value(knapsack_max_weight, items):

    # Create the lookup table
    lookup_table = [0] * (knapsack_max_weight + 1)

    print(reversed(range(knapsack_max_weight + 1)))

    # Iterate over items
    for item in items:

        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]

for test in tests:
    assert test['correct_output'] == max_value(**test['input'])
