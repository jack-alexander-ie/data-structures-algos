# Ref. 1: https://gist.github.com/jamiees2/5531924
# Ref. 2: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# Ref. 3: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

from helpers import load_map, show_map
import heapq
from math import sqrt, sin, cos, sqrt, atan2, radians
import time


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __gt__(self, other):
        return self.f > other.f


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


def create_path(current_intersection):
    """
    Work backwards from the target -> go from each child to its parent until you reach the start
    """
    path = []
    current = current_intersection
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def shortest_path(graph, start, goal):

    start_node = Node(None, start)

    frontier = [start_node]                                         # init frontier with start node
    explored = [False for _ in range(len(graph.intersections)+1)]   # init explored

    goal_coordinates = graph.intersections[goal]                    # goal coordinates

    while frontier:

        current_intersection = heapq.heappop(frontier)              # pop off vertex with least f
        explored[current_intersection.position] = True              # mark explored

        print('Current:', str(current_intersection.position),
              '\t G:' + str(current_intersection.g),
              '\t H:' + str(current_intersection.h),
              '\t F:' + str(current_intersection.f) + '\n')

        if current_intersection.position == goal:                   # if goal...
            return create_path(current_intersection)                # ...create path & return it

        current_coordinates = graph.intersections[current_intersection.position]  # grab its coordinates

        for neighbour in graph.roads[current_intersection.position]:              # for each neighbour

            if explored[neighbour]:                                 # if already explored, move to next
                continue

            neighbour_coordinates = graph.intersections[neighbour]  # grab neighbour coordinates

            neighbour_node = Node(current_intersection, neighbour)  # create neighbour node
            neighbour_node.g = current_intersection.g + euclidean_distance(current_coordinates, neighbour_coordinates)  # calc g cost
            neighbour_node.h = euclidean_distance(neighbour_coordinates, goal_coordinates)
            neighbour_node.f = neighbour_node.g + neighbour_node.h

            if neighbour_node in frontier:                          # neighbour in frontier
                new_g = current_intersection.g + neighbour_node.g
                if neighbour_node.g > new_g:
                    neighbour_node.g = new_g
                continue

            heapq.heappush(frontier, neighbour_node)                # neighbour not in frontier, add it

            print('Neighbour:', str(neighbour),
                  '\t G:' + str(neighbour_node.g),
                  '\t H:' + str(neighbour_node.h),
                  '\t F:' + str(neighbour_node.f) + '\t')

            time.sleep(2)

        print()
        print('-'*20)

    raise RuntimeError("No solution found")


map_40 = load_map('map-40.pickle')
path = shortest_path(map_40, 8, 24)
print()
print('Path:', path, '\n')          # Should be: [8, 14, 16, 37, 12, 17, 10, 24]
# show_map(map_40, 8, 24, path)     # Returning: [8, 30, 16, 37, 12, 17, 10, 24]
