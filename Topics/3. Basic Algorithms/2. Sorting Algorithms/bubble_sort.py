""" Two different bubble sort implementations


.....

"""


def bubble_sort_1(list_of_nums):

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


wakeup_times = [16, 49, 3, 12, 56, 49, 55, 22, 13, 46, 19, 55, 46, 13, 25, 56, 9, 48, 45]
bubble_sort_1(wakeup_times)
print("Pass" if (wakeup_times[0] == 3) else "Fail")

print(wakeup_times)
