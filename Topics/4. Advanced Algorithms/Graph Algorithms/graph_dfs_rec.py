# This uses an Adjacency List representation to store the graph


class Node:
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_node):
        if del_node in self.children:
            self.children.remove(del_node)


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


nodeG = Node('G')
nodeR = Node('R')
nodeA = Node('A')
nodeP = Node('P')
nodeH = Node('H')
nodeS = Node('S')

graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])

graph1.add_edge(nodeG, nodeR)
graph1.add_edge(nodeA, nodeR)
graph1.add_edge(nodeA, nodeG)
graph1.add_edge(nodeR, nodeP)
graph1.add_edge(nodeH, nodeG)
graph1.add_edge(nodeH, nodeP)
graph1.add_edge(nodeS, nodeR)


def test_graph(graph):
    """ Verifies that the graph is created accurately by printing all parent and child nodes """
    for each in graph.nodes:
        print('parent node = ', each.value, end='\nchildren\n')
        for each in each.children:
            print(each.value, end=' ')
        print('\n')


# test_graph(graph1)


def dfs_recursion_start(self, start_node):
    visited = {}
    self.dfs_recursion(start_node, visited)


def dfs_recursion(self, node, visited):
    if node == None:
        return False

    visited[node.value] = True
    print(node.value)

    for each in node.children:
        if (each.value not in visited):
            self.dfs_recursion(each, visited)


Graph.dfs_recursion_start = dfs_recursion_start
Graph.dfs_recursion = dfs_recursion
graph1.dfs_recursion_start(nodeG)
