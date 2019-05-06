class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """

    open_stack, close_stack = Stack(), Stack()

    stack = Stack()

    for char in equation:

        if char is '(':
            stack.push(char)
        elif char is ')':
            # Auto pops for comparison
            if stack.pop() == None:
                return False

    if stack.size() == 0:
        return True

    return False


print(equation_checker('((3^2 + 8)*(5/2))/(2+6)'))
print(equation_checker('((3^2 + 8)*(5/2))/(2+6))'))
