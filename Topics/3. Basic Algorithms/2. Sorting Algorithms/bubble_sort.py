""" Two different bubble sort implementations """


def bubble_sort_1(list_of_nums):
    """ In place sorting of numbers """

    list_length = len(list_of_nums)

    for i in range(list_length):                      # Traverse through elements
        swapped = False

        range_max = list_length - i - 1

        for j in range(0, range_max):                 # Traverse from 0 to n-i-1. Swap if element found > next element

            if list_of_nums[j] > list_of_nums[j + 1]:
                list_of_nums[j], list_of_nums[j + 1] = list_of_nums[j + 1], list_of_nums[j]
                swapped = True

        if swapped is False:                # If no elements swapped, break
            break


# wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
# bubble_sort_1(wakeup_times)
# print("Pass" if (wakeup_times[0] == 3) else "Fail")


# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def bubble_sort_2(list_of_times):
    """ In place sorting of times """

    list_length = len(list_of_times)

    for i in range(list_length):  # Traverse through elements
        swapped = False

        range_max = list_length - i - 1

        for j in range(0, range_max):  # Traverse from 0 to n-i-1. Swap if element found > next element

            if list_of_times[j] < list_of_times[j + 1]:
                list_of_times[j], list_of_times[j + 1] = list_of_times[j + 1], list_of_times[j]
                swapped = True

        if swapped is False:  # If no elements swapped, break
            break


print(sleep_times)
bubble_sort_2(sleep_times)
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")
print(sleep_times)
