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


def pre_order_with_stack_buggy(tree):

    visit_order = list()
    stack = Stack()

    node = tree.get_root()

    stack.push(node)
    node = stack.top()

    visit_order.append(node.get_value())

    count = 0
    loop_limit = 7

    while node and count < loop_limit:

        print(f"""loop count: {count} current node: {node} stack: {stack}""")

        count += 1

        # Issue here when going back up
        # node.has_left_child may always be true
        # Check to make sure it's not already been checked
        if node.has_left_child():

            if node.get_left_child().value in visit_order:
                # Implement check here
                stack.pop()

            else:
                node = node.get_left_child()
                stack.push(node)
                node = stack.top()
                visit_order.append(node.get_value())

        elif node.has_right_child():

            if node.get_right_child.value in visit_order:
                # Implement change here
                stack.pop()

            else:
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


tr = Tree("apple")
tr.get_root().set_left_child(Node("banana"))
tr.get_root().set_right_child(Node("cherry"))
tr.get_root().get_left_child().set_left_child(Node("dates"))

pre_order_with_stack_buggy(tr)
