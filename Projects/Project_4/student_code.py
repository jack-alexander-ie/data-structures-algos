from helpers import load_map, show_map
import heapq
from math import sqrt, sin, cos, sqrt, atan2, radians


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


def calc_cost(start_point, end_point):
    """
    Helper function to calculate the distance between two points.
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
    goal_node = Node(None, goal)

    frontier = [start_node]                                         # init frontier with start node
    explored = [False for _ in range(len(graph.intersections)+1)]   # init explored

    goal_coordinates = graph.intersections[goal]                    # goal coordinates

    while frontier:

        current_intersection = heapq.heappop(frontier)              # pop off vertex with least f
        explored[current_intersection.position] = True              # mark explored

        if current_intersection == goal:                            # if goal...
            return create_path(current_intersection)                #...create path & return it

        current_coordinates = graph.intersections[current_intersection.position]  # grab its coordinates

        for neighbour in graph.roads[current_intersection.position]:              # for each neighbour

            if explored[neighbour]:                                 # if explored, move to next
                continue

            neighbour_coordinates = graph.intersections[neighbour]  # grab neighbour coordinates

            neighbour_node = Node(current_intersection, neighbour)  # Create a node for the neighbour
            neighbour_node.g = current_intersection.g + calc_cost(current_coordinates, neighbour_coordinates)  # calc g cost
            neighbour_node.h = euclidean_distance(neighbour_coordinates, goal_coordinates)
            neighbour_node.f = neighbour.g + neighbour.h

            if neighbour_node in frontier:              # neighbour in frontier
                """
                If it is on the open list already, check to see if this path to that square is better, 
                using G cost as the measure. A lower G cost means that this is a better path. If so, 
                change the parent of the square to the current square, and recalculate the G and F 
                scores of the square. If you are keeping your open list sorted by F score, you may need 
                to resort the list to account for the change.
                """
                continue

            heapq.heappush(frontier, neighbour_node)    # neighbour not in frontier, add it

    raise RuntimeError("No solution found")


map_40 = load_map('map-40.pickle')

path = shortest_path(map_40, 5, 34)             # [5, 16, 37, 12, 34]

print(path)
# show_map(map_40, start=5, goal=34, path=path)
