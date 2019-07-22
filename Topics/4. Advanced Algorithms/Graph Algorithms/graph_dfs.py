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


def dfs_search_test(root: GraphNode, target: any) -> GraphNode:
    """ Executes a depth first search of a graph """
    visited_stack = []
    current_node = root
    while current_node:
        if current_node.value is target:            # Check if current node is target value
            return current_node
        if current_node not in visited_stack:       # Add it to the stack
            visited_stack.append(current_node)
        if current_node.children is not []:         # Check if it has children
            for child in current_node.children:     # Choose an edge
                if child not in visited_stack:      # Only visit if it's not already in the stack
                    if child.value is target:       # Return the node if target found
                        return child
                    current_node = child
        else:
            current_node = visited_stack.pop()      # Go back to previous node if no children


# assert nodeA == dfs_search_test(nodeS, 'A')
# assert nodeS == dfs_search_test(nodeP, 'S')
# assert nodeR == dfs_search_test(nodeH, 'R')


def dfs_search(root_node, search_value):
    visited = []
    stack = [root_node]

    while len(stack) > 0:
        current_node = stack.pop()
        visited.append(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                stack.append(child)


assert nodeA == dfs_search(nodeS, 'A')
assert nodeS == dfs_search(nodeP, 'S')
assert nodeR == dfs_search(nodeH, 'R')
