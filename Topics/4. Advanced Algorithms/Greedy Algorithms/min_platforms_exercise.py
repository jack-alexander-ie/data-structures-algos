"""
Problem Statement:

Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of
platforms required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as int hhmm for e.g. 9:30 -> 930, 13:45 -> 1345
"""


def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival times
    :param: departure - list of departure times
    TODO: Return min. number of platforms required so that no train has to wait for others to leave
    """

    arrival = sorted(arrival)
    departure = sorted(departure)

    events = []

    for time in arrival:
        events.append((time, 'arr'))

    for time in departure:
        events.append((time, 'dep'))

    events = sorted(events)

    max_platforms, platform_tracker = 0, 0

    for event in events:

        if event[1] is 'arr':

            platform_tracker += 1

            if platform_tracker >= max_platforms:
                max_platforms = platform_tracker

        else:
            platform_tracker -= 1

    return max_platforms


arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]

min_platforms(arrival, departure)


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# arrival = [900,  940, 950,  1100, 1500, 1800]
# departure = [910, 1200, 1120, 1130, 1900, 2000]
# test_case = [arrival, departure, 3]
# test_function(test_case)

# arrival = [200, 210, 300, 320, 350, 500]
# departure = [230, 340, 320, 430, 400, 520]
# test_case = [arrival, departure, 2]
# test_function(test_case)
