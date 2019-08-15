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

    parents = {}

    items = []                                                      # TODO: remove, debug only

    while frontier:

        current_intersection = min(frontier.keys(), key=(lambda k: frontier[k]))    # grab vertex with least f
        current_cost = frontier[current_intersection]                               # grab cost

        # items.append(current_intersection)                          # TODO: remove, debug only

        if current_intersection == goal:                            # if goal, create path & return it
            # return create_path(explored)
            # return items                                            # TODO: remove, debug only
            """
            Save the path. Working backwards from the target square, 
            go from each square to its parent square until you reach 
            the starting square. That is your path.
            """
            pass

        del frontier[current_intersection]                          # remove from frontier
        explored[current_intersection] = True                       # mark explored

        current_coordinates = graph.intersections[current_intersection]  # grab its coordinates

        for neighbour in graph.roads[current_intersection]:         # for each neighbour

            if explored[neighbour]:                                 # if explored, move to next
                continue

            neighbour_coordinates = graph.intersections[neighbour]  # grab neighbour coordinates

            # G is the distance between the current node and the start node.
            neighbour_g = current_cost + calc_cost(current_coordinates, neighbour_coordinates)  # calc g cost

            if neighbour in frontier:                               # if neighbour is in the frontier

                """
                If in the open list: 
                    1. Check to see if this path to that square is better, using G cost as the measure. 
                       A lower G cost means that this is a better path. 
                    2. If so: 
                        2.1 change the parent of the square to the current square
                        2.2 recalculate the G and F scores of the square  
                    3. If you are keeping your open list sorted by F score, resort the list
                """

                new_neighbour_g = current_cost + neighbour_g        # cal the new g value

                if frontier[neighbour] > new_neighbour_g:           # lower G cost means that this is a better path
                    frontier[neighbour] = new_neighbour_g           # set new g as value
                    parents[current_intersection] = neighbour

            else:                                                   # if neighbour is not

                """
                If not in the open list: 
    
                    1. add it to the open list. 
                    2. make the current square the parent of this square 
                    3. record the F, G, and H costs of the square.
                """

                # H is the estimated distance from the current node to the end node.
                neighbour_h = euclidean_distance(neighbour_coordinates, goal_coordinates)

                # F is the total cost of the node
                neighbour_f = neighbour_g + neighbour_h

                # Add it to the frontier, along with its f cost
                frontier[neighbour] = neighbour_f

                # Make current square parent of neighbour square
                parents[current_intersection] = neighbour

    raise RuntimeError("No solution found")


map_40 = load_map('map-40.pickle')

path = shortest_path(map_40, 5, 34)             # [5, 16, 37, 12, 34]

print(path)
# show_map(map_40, start=5, goal=34, path=path)
