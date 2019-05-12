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


class State:

    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node} visited_left: {self.visited_left} visited_right: {self.visited_right}"""
        return s


def pre_order_with_stack_buggy(tree):
    visit_order = list()
    stack = Stack()

    node = tree.get_root()

    stack.push(node)
    node = stack.top()

    visit_order.append(node.get_value())

    while node:

        # Issue here when going back up
        # node.has_left_child may always be true
        # Check to make sure it's not already been checked
        if node.has_left_child() and node.get_left_child().value not in visit_order:

            node = node.get_left_child()
            stack.push(node)
            node = stack.top()
            visit_order.append(node.get_value())

        elif node.has_right_child() and node.get_right_child().value not in visit_order:

            node = node.get_right_child()
            stack.push(node)
            node = stack.top()
            visit_order.append(node.get_value())

        else:

            stack.pop()

            if not stack.is_empty():
                node = stack.top()
            else:
                node = None

    return visit_order


def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack = Stack()

    node = tree.get_root()
    visit_order.append(node.get_value())

    # Create a state and push it onto the node instead of raw node
    state = State(node)
    stack.push(state)

    count = 0

    while node:

        if debug_mode:
            print(f"""loop count: {count} current node: {node} stack: {stack}""")

        count += 1

        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            visit_order.append(node.get_value())
            state = State(node)
            stack.push(state)

        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            visit_order.append(node.get_value())
            state = State(node)

        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None

    if debug_mode:
        print(f"""loop count: {count} current node: {node} stack: {stack}""")

    return visit_order


tr = Tree("apple")
tr.get_root().set_left_child(Node("banana"))
tr.get_root().set_right_child(Node("cherry"))
tr.get_root().get_left_child().set_left_child(Node("dates"))

# Fixed but not the way it should be
# pre_order_with_stack_buggy(tr)
# pre_order_with_stack(tr, debug_mode=True)
