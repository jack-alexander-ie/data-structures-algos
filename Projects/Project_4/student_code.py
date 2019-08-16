# Ref. 1: https://gist.github.com/jamiees2/5531924
# Ref. 2: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

from helpers import load_map, show_map, Map
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
        return self.position == other

    def __gt__(self, other):
        return self.f > other.f

    def __hash__(self):
        return hash(self.position)


def distance(neighbour: List[float], goal: List[float]) -> float:
    """
    A heuristic function which calculates the Euclidean Distance between two points

    :param neighbour: coordinates of the neighbouring vertex
    :param goal: coordinates of the goal vertex
    :return: the euclidean distance
    """
    x1, y1 = neighbour[0], neighbour[1]
    x2, y2 = goal[0], goal[1]
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


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

    # frontier = set()                                                              # init the frontier
    # frontier.add(start_node)                                                      # add the start node

    frontier = dict()                                                             # init the frontier
    frontier[start] = start_node                                                  # add the start start node

    explored = [False for _ in range(len(graph.intersections)+1)]                 # init explored

    goal_coordinates = graph.intersections[goal]                                  # goal coordinates

    while frontier:

        print('Frontier:', sorted(frontier.keys()), '\n')

        # current_intersection = min(frontier, key=lambda o: o.f)                   # grab vertex with least f
        # frontier.remove(current_intersection)                                     # remove it from the frontier

        current_intersection = sorted(frontier.values())[0]                       # grab vertex with least f
        del frontier[current_intersection.position]                               # remove it from the frontier

        print('Current:', current_intersection.position,
              '\t F:', str(current_intersection.f),
              '\t G:', str(current_intersection.g),
              '\t H:', str(current_intersection.h), '\n')

        print('Neighbours:', graph.roads[current_intersection.position], '\n')

        explored[current_intersection.position] = True                            # mark as explored

        if current_intersection.position == goal:                                 # if goal reached...
            return create_path(current_intersection)                              # ...create path & return it

        current_coordinates = graph.intersections[current_intersection.position]  # grab its coordinates

        for neighbour in graph.roads[current_intersection.position]:              # for each neighbour

            if explored[neighbour]:                                               # already explored, move to next
                continue

            neighbour_coordinates = graph.intersections[neighbour]                # grab neighbour coordinates

            new_g_score = current_intersection.g + distance(current_coordinates, neighbour_coordinates)  # calc new g

            if neighbour in frontier:                                             # neighbour in frontier
                # print(frontier[neighbour])
                # if new_g_score < frontier[neighbour].g:                           # if new g < neighbours old g...
                #     print('---- UPDATED G VALUE ----')
                #     neighbour_node.g = new_g_score                                # ...update old g (better path)

                if new_g_score < frontier[neighbour].g:                           # if new g < neighbours old g...
                    print()
                    print('\t\tUPDATING G VALUE:', neighbour, '\n')
                    frontier[neighbour].g = new_g_score                           # ...update old g (better path)
                    frontier[neighbour].parent = current_intersection
                continue

            neighbour_node = Node(current_intersection, neighbour)  # create neighbour node
            neighbour_node.g = new_g_score
            neighbour_node.h = distance(neighbour_coordinates, goal_coordinates)
            neighbour_node.f = new_g_score + neighbour_node.h

            # frontier.add(neighbour_node)                                          # add neighbour to frontier
            frontier[neighbour] = neighbour_node

            print('Neighbour:', neighbour_node.position,
                  '\t F:', str(neighbour_node.f),
                  '\t G:', str(neighbour_node.g),
                  '\t H:', str(neighbour_node.h))
        print()
        print('-'*20, '\n')

    raise RuntimeError("No solution found")


print()
map_40 = load_map('map-40.pickle')
# print('Path:', shortest_path(map_40, 5, 34), '\n')      # Correct Answer: [5, 16, 37, 12, 34]
# print('Path:', shortest_path(map_40, 5, 5), '\n')       # Correct Answer: [5]
print('Path:', shortest_path(map_40, 8, 24), '\n')      # Correct Answer: [8, 14, 16, 37, 12, 17, 10, 24]

# show_map(M, start=None, goal=None, path=None):
# show_map(map_40, 8, 24, shortest_path(map_40, 8, 24))
