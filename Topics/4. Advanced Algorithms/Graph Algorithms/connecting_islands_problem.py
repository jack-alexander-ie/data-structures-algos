import heapq


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to return minimum cost of connecting all islands
    """

    # TODO: Implement Dijkstra's algorithm using a prio queue

    pass


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
# solution = 6

print(get_minimum_cost_of_connecting(num_islands, bridge_config))
