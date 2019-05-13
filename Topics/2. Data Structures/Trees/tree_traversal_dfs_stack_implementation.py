"""
    'Traversing' a tree: visiting all nodes once

    Used for: search, insert, delete

    Two Types:

        1. Depth First Search (DFS)
        2. Breadth first Search (BFS)

    DFS:

        1. Pre-order: Check off node as you go along, left-most by convention
        2. In-order: Traverse to left-most leaf, check it off, move to parent, check it off, move to right leaf...
        3. Post-order: Same as for in-order, but only check off the parent after all children are checked off
"""


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


# Let's define a stack to help keep track of the tree nodes
class Stack:
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


# create a tree and add some nodes
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# Depth first, pre-order traversal with a stack
# Stack used to help keep track of the nodes visited
visit_order = list()
stack = Stack()

# start at the root node, visit it and then add it to the stack
node = tree.get_root()
stack.push(node)
visit_order.append(node.get_value())

# Start traversing
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

# Banana visited
visit_order.append(node.get_value())

print(node.value)

# If banana has a left child
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

# Visit dates - first leaf (no children)
visit_order.append(node.get_value())

# since "dates" has no children, start to retrace steps by popping it off the stack.
stack.pop()

# now set the node to the new top of the stack, which is banana
node = stack.top()
print(node)

# banana doesn't have a right child, so pop it off the stack
stack.pop()

# now track the new top of the stack, which is apple
node = stack.top()
print(node)

# All left side has been visited, no for right side and add to the stack
if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)

# visit cherry
visit_order.append(node.get_value())

# Now check if cherry has a left child
if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)
else:
    node = node.get_right_child()
    stack.push(node)

# since cherry has neither left nor right child nodes,
# we are done tracking it, and can pop it off the stack
stack.pop()

print(f"""visit_order {visit_order} stack {stack}""")

# now we're back to apple at the top of the stack.
# since we've already checked apple's left and right child nodes,
# we can pop apple off the stack

print(f"pop {stack.pop()} off stack")
print(f"pre-order traversal visited nodes in this order: {visit_order}")

print(f"""stack
{stack}""")