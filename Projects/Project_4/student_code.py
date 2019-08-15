# Ref. 1: https://gist.github.com/jamiees2/5531924
# Ref. 2: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
# Ref. 3: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

from helpers import load_map, show_map, Map
import heapq
from math import sqrt, sin, cos, sqrt, atan2, radians
from typing import List


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent        # it's parent intersection
        self.position = position    # intersection 'id'

        self.g = 0                  # dist: start -> point
        self.h = 0                  # est. dist: point -> goal
        self.f = 0                  # dist: (start -> point) + (est. dist point -> goal)

    def __eq__(self, other):
        return self.position == other.position

    def __gt__(self, other):
        return self.f > other.f


def distance(neighbour: List[float], goal: List[float]) -> float:
    """
    A heuristic function which calculates the Euclidean Distance between two points

    :param neighbour: coordinates of the neighbouring vertex
    :param goal: coordinates of the goal vertex
    :return: the euclidean distance
    """
    x1, y1 = neighbour[0], neighbour[1]
    x2, y2 = goal[0], goal[1]
    return sqrt(((x1 - x2)**2) + ((y1 - y2)**2))


def create_path(goal_node: Node) -> List[int]:
    """
    Creates a path from the goal node to the start node

    :param goal_node: goal node reached
    :return: a list of ints which is the path
    """
    path = []
    current = goal_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]


def shortest_path(graph: Map, start: int, goal: int) -> List[int]:
    """
    Finds the shortest path between two points using the A* Search algorithm

    :param graph: the graph to traverse
    :param start: the starting intersection
    :param goal: the goal intersection
    :return: a list of integers representing the optimal intersections to go through
    """

    start_node = Node(None, start)                                                # create the start node

    frontier = [start_node]                                                       # init frontier with start node
    explored = [False for _ in range(len(graph.intersections)+1)]                 # init explored

    goal_coordinates = graph.intersections[goal]                                  # goal coordinates

    while frontier:

        current_intersection = heapq.heappop(frontier)                            # pop off vertex with least f
        explored[current_intersection.position] = True                            # mark explored

        if current_intersection.position == goal:                                 # if goal reached...
            return create_path(current_intersection)                              # ...create path & return it

        current_coordinates = graph.intersections[current_intersection.position]  # grab its coordinates

        for neighbour in graph.roads[current_intersection.position]:              # for each neighbour

            if explored[neighbour]:                                               # if already explored, move to next
                continue

            neighbour_coordinates = graph.intersections[neighbour]                # grab neighbour coordinates
            neighbour_node = Node(current_intersection, neighbour)                # create neighbour node

            neighbour_node.g = current_intersection.g + distance(current_coordinates, neighbour_coordinates)
            neighbour_node.h = distance(neighbour_coordinates, goal_coordinates)
            neighbour_node.f = neighbour_node.g + neighbour_node.h

            if neighbour_node in frontier:                                        # neighbour in frontier
                new_g = current_intersection.g + neighbour_node.g                 # calc new g
                if neighbour_node.g > new_g:                                      # if new g < neighbours old g...
                    neighbour_node.g = new_g                                      # ...update neighbours old g (better)

            heapq.heappush(frontier, neighbour_node)                              # add neighbour to frontier

    raise RuntimeError("No solution found")


map_40 = load_map('map-40.pickle')
print('Path:', shortest_path(map_40, 5, 34), '\n')      # [5, 16, 37, 12, 34]
print('Path:', shortest_path(map_40, 5, 5), '\n')       # [5]
print('Path:', shortest_path(map_40, 8, 24), '\n')      # [8, 14, 16, 37, 12, 17, 10, 24]
