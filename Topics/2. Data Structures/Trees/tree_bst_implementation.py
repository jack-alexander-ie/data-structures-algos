from collections import deque


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
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Queue:
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert_with_loop(self, new_value):

        new_node = Node(new_value)

        # Check to see if tree is empty
        if self.root is None:
            self.root = new_node
            return

        node = self.root

        while True:

            comparison = self.compare(node, new_node)

            if comparison is 0:
                # Overwrite old value
                node.set_value(new_node.get_value())
                break

            elif comparison is -1:

                if node.get_left_child() is None:
                    node.set_left_child(new_node)
                    break
                else:
                    node = node.get_left_child()

            elif comparison is 1:

                if node.get_right_child() is None:
                    node.set_right_child(new_node)
                    break
                else:
                    node = node.get_right_child()

    def insert_with_recursion(self, value):

        insert_new_node = Node(value)

        if self.root is None:
            self.root = insert_new_node
            return

        root = self.root

        def traverse(node, new_node):

            if node:

                comparison = self.compare(node, new_node)

                if comparison is 0:
                    # Overwrite existing value
                    node.set_value(new_node.get_value())
                    return

                elif comparison is -1:

                    if node.get_left_child() is None:
                        node.set_left_child(new_node)
                    else:
                        traverse(node.get_left_child(), new_node)

                elif comparison is 1:

                    if node.get_right_child() is None:
                        node.set_right_child(new_node)
                    else:
                        traverse(node.get_right_child(), new_node)

        traverse(root, insert_new_node)

    def insert(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node is None:
            self.root = new_node
            return

        while True:
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break  # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break  # inserted node, so stop looping
            else:  # comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break  # inserted node, so stop looping

    def search(self, value):

        node = self.root

        while node:

            if node.value == value:
                return True

            elif value < node.value:

                node = node.get_left_child()

            elif value > node.value:

                node = node.get_right_child()

        return False

    def delete(self, value):

        # Base Check
        if self.root is None:
            return self.root

        node = self.root
        parent = node

        while node:

            if node.value == value:

                # If node is a leaf
                if node.get_left_child() is None and node.get_right_child() is None:

                    # Check which branch the node belongs to
                    if node.value is parent.get_left_child().value:
                        parent.set_left_child(None)
                    else:
                        parent.set_right_child(None)
                    break

                # If node has two children
                elif node.get_left_child() is not None and node.get_right_child() is not None:
                    print('\n Node has two children \n')
                    break

                # If node has one child
                else:
                    if node.get_left_child() is not None:
                        if node is parent.get_left_child():
                            parent.set_left_child(node.get_left_child())
                    else:
                        parent.set_right_child(node.get_right_child())
                    break

            elif value < node.value:

                parent = node
                node = node.get_left_child()

            elif value > node.value:

                parent = node
                node = node.get_right_child()

        return False

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:

            node, level = q.deq()

            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level

        return s


# tree = Tree()
# tree.insert_with_loop(5)
# tree.insert_with_loop(6)
# tree.insert_with_loop(4)
# tree.insert_with_loop(2)
# tree.insert_with_loop(5)  # insert duplicate
# print('Looped Insert:', tree)

# tree = Tree()
# tree.insert_with_recursion(5)
# tree.insert_with_recursion(6)
# tree.insert_with_recursion(4)
# tree.insert_with_recursion(2)
# tree.insert_with_recursion(5)  # insert duplicate
# print('Recursive Insert:', tree)

# Tree Search
tree = Tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(7)

# print(f"""search for 8: {tree.search(8)}""")
# print(f"""search for 2: {tree.search(2)}""")
# print(tree)

tree.delete(5)
print(tree)
