import time


class GraphNode:
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)

    def print_children(self):
        for child in self.children:
            print('Current Nodes Child:', child.value)


class Graph:
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)


nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)


def dfs_search(root_node, search_value):
    """ Executes a depth first search of a graph """

    current_node = root_node

    while current_node:

        print('Current Node:', current_node.value)
        current_node.print_children()
        print('\n')

        for child in current_node.children:

            if child.value is search_value:
                print("Search successful, found '" + search_value + "', returning the node")
                return child
            current_node = child

            time.sleep(1)


# assert nodeA == dfs_search(nodeS, 'A')
assert nodeS == dfs_search(nodeP, 'S')      # Cyclic route happening -> P, R, H, G
# assert nodeR == dfs_search(nodeH, 'R')
