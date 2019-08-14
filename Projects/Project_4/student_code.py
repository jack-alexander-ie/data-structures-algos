from helpers import load_map, show_map
import heapq
from math import sqrt, sin, cos, sqrt, atan2, radians


def calc_cost(start_point, end_point):
    """
    Helper function to calculate the dostance between two points.
    Ref. from https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude/43211266#43211266

    :param start_point: the coordinates of the start point
    :param end_point: the coordinated of the end point
    :return: the distance in km between two points
    """
    R = 6373.0                                      # approx. radius of earth in km
    lat1, lon1 = start_point[0], start_point[1]     # unpack start coordinates
    lat2, lon2 = end_point[0], end_point[1]         # unpack end coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return int(distance)


def euclidean_distance(neighbour, goal):
    """
    A heuristic function which calculates the Euclidean Distance
    :param neighbour: coordinates of the neighbouring vertex
    :param goal: coordinates of the goal vertex
    :return: the euclidean distance
    """
    x1, y1 = neighbour[0], neighbour[1]
    x2, y2 = goal[0], goal[1]
    return sqrt(((x1 - x2)**2) + ((y1 - y2)**2))


def create_path(explored):

    return explored.keys()

    optimal_path = list()
    while current.parent:
        optimal_path.append(current)
        current = current.parent
    optimal_path.append(current)
    return optimal_path[::-1]


def shortest_path(graph, start, goal):

    frontier = dict()                                               # init frontier - (cost, frontier)
    explored = [False for _ in range(len(graph.intersections)+1)]   # init explored
    frontier[start] = 0                                             # add the start to the set
    goal_coordinates = graph.intersections[goal]                    # goal coordinates

    items = []                                                      # TODO: remove, debug only

    while frontier:

        current_intersection = min(frontier.keys(), key=(lambda k: frontier[k]))    # grab vertex with least f
        current_cost = frontier[current_intersection]                               # grab cost

        items.append(current_intersection)                          # TODO: remove, debug only

        if current_intersection == goal:                            # if goal, create path & return it
            # return create_path(explored)
            return items                                            # TODO: remove, debug only

        del frontier[current_intersection]                          # remove from frontier
        explored[current_intersection] = True                       # mark explored

        current_coordinates = graph.intersections[current_intersection]  # grab its coordinates

        for neighbour in graph.roads[current_intersection]:         # for each neighbour

            if explored[neighbour]:                                 # if explored, move to next
                continue

            neighbour_coordinates = graph.intersections[neighbour]  # grab neighbour coordinates
            neighbour_g = current_cost + calc_cost(current_coordinates, neighbour_coordinates)  # calc g cost

            if neighbour in frontier:
                new_g = current_cost + neighbour_g
                if frontier[neighbour] > new_g:
                    frontier[neighbour] = new_g
            else:
                neighbour_h = euclidean_distance(neighbour_coordinates, goal_coordinates)
                neighbour_f = neighbour_g + neighbour_h
                frontier[neighbour] = neighbour_f

    raise RuntimeError("No solution found")


map_40 = load_map('map-40.pickle')

path = shortest_path(map_40, 5, 34)             # [5, 16, 37, 12, 34]
show_map(map_40, start=5, goal=34, path=path)
