import math


class GraphEdge:
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class GraphNode:
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)


class Graph:
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


# Create all the nodes
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

# Create the graph
graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])

# Add the edges
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_u, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_u, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_d, 4)
graph.add_edge(node_c, node_u, 6)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_a, 7)
graph.add_edge(node_i, node_c, 4)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_c, 5)
graph.add_edge(node_t, node_y, 5)
graph.add_edge(node_y, node_i, 4)
graph.add_edge(node_y, node_t, 5)


def dijkstra(start_node: GraphNode, end_node: GraphNode) -> int:

    # Create a dict with nodes from the created graph, values for which are infinite
    distance_dict = {node: math.inf for node in graph.nodes}

    # Dict to store the shortest path
    shortest_path_to_node = {}

    # Set start nodes inf value to zero
    distance_dict[start_node] = 0

    # while there are values in the dict
    while distance_dict:

        # Sorts dict based on node weight - sorts from min, grabs 0th value and unpacks tuple to vars
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]

        # Add the min node to the shortest path by popping it out of the dict
        shortest_path_to_node[current_node] = distance_dict.pop(current_node)

        # Cycle through the edges in the current node
        for edge in current_node.edges:

            # Check of the edges node exists in the distance dict
            if edge.node in distance_dict:

                # Update all nodes with the latest distance
                new_node_distance = node_distance + edge.distance

                # Update the value of the node's distance if it's greater than the new distance
                if distance_dict[edge.node] > new_node_distance:
                    distance_dict[edge.node] = new_node_distance

    return shortest_path_to_node[end_node]


print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(node_u, node_y)))

import heapq


def dijkstra_prio(start_node: GraphNode, end_node: GraphNode) -> int:

    """
    This function needs to be converted so that it can be used for the connecting islands problem.

    Refer back to notes.
    """

    heap = [(node, math.inf) for node in graph.nodes]

    print(heap)

    distance_dict = []

    shortest_path_to_node = []

    distance_dict[start_node] = 0

    while distance_dict:

        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]

        shortest_path_to_node[current_node] = distance_dict.pop(current_node)

        for edge in current_node.edges:

            if edge.node in distance_dict:

                new_node_distance = node_distance + edge.distance

                if distance_dict[edge.node] > new_node_distance:
                    distance_dict[edge.node] = new_node_distance

    return shortest_path_to_node[end_node]


# print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra_prio(node_u, node_y)))
