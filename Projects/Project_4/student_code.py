from helpers import load_map
import heapq
from math import sin, cos, sqrt, atan2, radians

map_40 = load_map('map-40.pickle')


def print_graph_info(graph):
    for intersection in graph.intersections.items():
        print('Intersection:', intersection)
    print('-' * 20)
    for road in graph.roads:
        print('Road:', road)
    print()


def calc_distance(start_point, end_point):
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
    return distance


def manhattan_distance(a, b):
    """
    The heuristic function which calculates the Manhatten Distance
    Ref. from https://www.redblobgames.com/pathfinding/a-star/implementation.html

    :param a: goal coordinates
    :param b: neighbour coordinates
    :return: heuristic distance
    """
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def shortest_path(graph, start, goal):
    frontier = [(0, start)]                          # init frontier - (cost, frontier)
    explored = [False for _ in graph.intersections]  # init dict to track explored vertices
    current_cost = 0                                 # track the current cost
    goal_coordinates = graph.intersections[goal]
    path = []                                        # final path that will be returned

    while len(frontier) > 0:

        # print('Prio queue:', frontier)

        cost, current_vertex = heapq.heappop(frontier)              # Grab prio vertex

        current_coordinates = graph.intersections[current_vertex]   # Grab coordinates

        current_cost += cost                                        # add cost to total

        if current_vertex == goal:                                  # break if goal reached
            path.append(goal)
            break

        for neighbour in graph.roads[current_vertex]:               # for each neighbour
            # f(n) = g(n) + h(n)
            neighbour_coordinates = graph.intersections[neighbour]  # Grab coordinates

            g = int(calc_distance(current_coordinates, neighbour_coordinates))  # Calc g(n)

            #next_cost = current_cost + g

            if not explored[neighbour]:

                # print(neighbour_cost, neighbour)
                h = manhattan_distance(goal_coordinates, neighbour_coordinates)
                f = g + h

                heapq.heappush(frontier, (f, neighbour))
                # heapq.heappush(frontier, (cost + neighbour_cost, neighbour))

                explored[current_vertex] = True                     # Add curr. vertex to explored

        path.append(current_vertex)                         # Update path

    return path


# shortest_path(map_40, 5, 34)
print('Path:', shortest_path(map_40, 5, 34))
