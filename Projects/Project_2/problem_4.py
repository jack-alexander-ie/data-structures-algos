"""
TODO: Test Cases
    1.
    2.
    3.
"""


class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    See if user is in a group
    :param user: user string (name/id)
    :param group: Group object, group to check user membership against
    :return: boolean
    """
    if user in group.get_users():           # Base Case - if user is in a group, return true
        return True

    for group in group.get_groups():        # Search every group in the parent's group list
        r = is_user_in_group(user, group)   # Check every group recursively
        if r:                               # If found, also return true
            return True
    return False                            # User not found, return false


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
