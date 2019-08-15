# Ref. from: https://github.com/MJOAN/Udacity-P3/blob/master/a_star.py

import heapq
from collections import defaultdict
import math


def shortest_path(M, start, goal):
    openset = set()  # cite: 3
    openset.add(start)

    closedset = set()

    priority_queue = list()
    estimated_cost, actual_distance_cost = 0, 0
    heapq.heappush(priority_queue, (estimated_cost, start, actual_distance_cost))

    came_from = defaultdict()

    f = defaultdict()
    f[start] = calculate_heuristic(M, start, goal)

    while len(openset) > 0:
        (estimated_cost, current, actual_distance_cost) = heapq.heappop(priority_queue)

        if current in openset:
            openset.remove(current)
        else:
            continue

        closedset.add(current)

        if current == goal:
            return a_star_search_path(came_from, current)  # cite: 2

        for neighbor in M.roads[current]:

            if neighbor in closedset:
                continue

            new_cost = actual_distance_cost + calculate_heuristic(M, current, neighbor)
            cost_from_neighbor = get_neighbor_cost(priority_queue, neighbor)

            if neighbor not in openset or new_cost < cost_from_neighbor:
                cost_from_neighbor = new_cost
                came_from[neighbor] = current

                f[neighbor] = new_cost + calculate_heuristic(M, neighbor, goal)
                heapq.heappush(priority_queue, (f[neighbor], neighbor, cost_from_neighbor))
                openset.add(neighbor)

    return "No path found."


def get_neighbor_cost(priority_queue, neighbor):
    for i in priority_queue:
        if i[1] == neighbor:
            item = priority_queue[0][2]
            return item


def a_star_search_path(came_from, current):
    path = [current]
    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
    return path[::-1]


def calculate_heuristic(M, intersection1, intersection2):  # cite: 1
    current_x_y = M.intersections[intersection1]
    neighbor_x_y = M.intersections[intersection2]
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(current_x_y, neighbor_x_y)]))
