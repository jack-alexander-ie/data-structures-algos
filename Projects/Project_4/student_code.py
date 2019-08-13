from helpers import load_map

map_40 = load_map('map-40.pickle')


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def shortest_path(graph, start, goal):

    def print_info():
        for intersection in graph.intersections.items():
            print(intersection)
        print('-' * 20)
        for road in graph.roads:
            print(road)

    pass


shortest_path(map_40, 5, 34)
