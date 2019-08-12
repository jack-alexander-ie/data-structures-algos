import heapq


def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    # Create a list of lists equalling the number of islands
    adjacency_list = [list() for _ in range(num_islands + 1)]

    print('Bridge Configs:', bridge_config, '\n')

    # Cycle through the configs
    for config in bridge_config:

        print('Bridge Config:', config)

        source, destination, cost = config[0], config[1], config[2]

        # For each source, append a tuple with destination and cost
        adjacency_list[source].append((destination, cost))

        # For each destination, append a tuple with source and cost -> destination also a source
        adjacency_list[destination].append((source, cost))

        print(adjacency_list, '\n\n')

    return adjacency_list


def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """

    print('-'*20, '\n')
    print('Graph:', graph, '\n')

    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1

    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]

    # initialize starting list - (edge_cost, neighbor)
    heap = [(0, start_vertex)]
    total_cost = 0

    while len(heap) > 0:

        print('Heap:', heap)

        # Strip off prio vertex, and sort
        cost, current_vertex = heapq.heappop(heap)

        print('Prio Pop:', (cost, current_vertex), '\n')

        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        # Add all the vertexes neighbours to the heap
        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(heap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    """
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)


num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
# solution = 6

print(get_minimum_cost_of_connecting(num_islands, bridge_config))
