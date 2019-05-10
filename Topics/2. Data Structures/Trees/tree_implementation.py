"""

    'Traversing' a tree: visiting all nodes once

    Used for: search, insert, delete

    Two Types:

        1. Depth First Search (DFS)
        2. Breadth first Search (BFS)

    DFS:

        1. Pre-order
        2. In-order
        3. Post-order

"""


class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left is None

    def has_right_child(self):
        return self.right is None


class Tree:

    # Insert value because you can't assume the user will know to init a node object.
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root
