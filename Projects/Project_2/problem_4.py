class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        assert type(group) == type(self)
        self.groups.append(group)

    def add_user(self, user: str):
        assert type(user) == str
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def print_group_names(self):
        if len(self.get_groups()) < 1:
            print('No subgroups found.')
        else:
            for group in self.get_groups():
                print(group.name)

    def print_user_names(self):
        if len(self.get_users()) < 1:
            print('No users found.')
        else:
            for user in self.get_users():
                print(user)


def is_user_in_group(user, group):
    """
    Check if a user is in a group
    :param user: user string (name/id)
    :param group: Group object, group to check user membership against
    :return: boolean
    """
    if user in group.get_users():               # Base Case - if user is in a group, return true
        return True

    for group in group.get_groups():            # Search every group in the parent's group list
        search = is_user_in_group(user, group)  # Check every group recursively
        if search:                              # If found, return true
            return True
    return False                                # User not found, return false


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Test Case 1 - Expected
parent.print_group_names()
child.print_group_names()
sub_child.print_group_names()
"""
Expected Output:

child
subchild
No subgroups found.
"""

# Test Case 2 - User added as group
# another_child = Group('Another child')
# parent.add_user(another_child)
"""
Expected Output: AssertionError - assert type(user) == str
"""

# Test Case 3 - Group added as user
# another_user = 'Another user'
# parent.add_group(another_user)
"""
Expected Output: AssertionError - assert type(group) == type(self)
"""
