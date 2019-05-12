class Node:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return "Node({})".format(self.get_value())

    def __str__(self):
        return "Node({})".format(self.get_value())


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


def pre_order(tree):

    # Initialise variables
    visit_order = list()
    root = tree.get_root()

    # Closure function
    def traverse(node):
        if node:
            # Visit node
            visit_order.append(node.value)
            # Traverse Left
            traverse(node.get_left_child())
            # Traverse Right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


def in_order(tree):

    # Initialise variables
    visit_order = list()
    root = tree.get_root()

    # Closure function
    def traverse(node):
        if node:
            # Traverse Left
            traverse(node.get_left_child())
            # Visit node
            visit_order.append(node.value)
            # Traverse Right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


def post_order(tree):

    # Initialise variables
    visit_order = list()
    root = tree.get_root()

    # Closure function
    def traverse(node):
        if node:
            # Traverse Left
            traverse(node.get_left_child())
            # Traverse Right
            traverse(node.get_right_child())
            # Visit node
            visit_order.append(node.value)

    traverse(root)

    return visit_order


tr = Tree("apple")
tr.get_root().set_left_child(Node("banana"))
tr.get_root().set_right_child(Node("cherry"))
tr.get_root().get_left_child().set_left_child(Node("dates"))

# Recursive solution
print(pre_order(tr))
print(in_order(tr))
print(post_order(tr))
