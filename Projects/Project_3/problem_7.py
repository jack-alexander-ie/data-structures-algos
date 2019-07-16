from collections import defaultdict
from typing import List


class RouteTrieNode:
    """ Stores individual part parts along with their handlers """

    def __init__(self, handler=None):
        """ Initialises the node with children and a handler """
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, path, handler=None):
        """ Inserts a new child path """
        if path in self.children:                         # Return None if path already exists
            print('Warning: Path already exists!')
            return
        else:
            self.children[path] = RouteTrieNode(handler)  # Add character if it doesn't exist


class RouteTrie:
    """ Stores routes and associated handlers """

    def __init__(self, root_handler=None):
        """ Initialises trie with a root node and root handler """
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_parts, handler):
        """ Recursively adds nodes to the trie """
        current_node = self.root
        for part in path_parts:                           # Traverse to the deepest node in the path
            current_node = current_node.children[part]    # defaultdict auto adds it if it doesn't already exist
        current_node.handler = handler                    # Assign the leaf a handler

    def find(self, path_parts):
        """ Finds if there is a path match """
        current_node = self.root                          # Start at the root
        for part in path_parts:                           # Cycle through the path parts
            if part not in current_node.children:         # If path doesn't exist...
                return                                    # ..return None
            current_node = current_node.children[part]    # Else, traverse onwards
        return current_node.handler                       # Return its handler


class Router:
    """ Wrapper for Trie and handlers """

    def __init__(self, root_handler, path_not_found):
        """ Creates a new RouteTrie for holding routes """
        if self.test_path(root_handler) and self.test_path(path_not_found):
            self.route_trie = RouteTrie(root_handler)           # Passes root handler to the initialised trie
            self.path_not_found = path_not_found                # Stores 404 not found response

    def add_handler(self, path, handler) -> None:
        """ Adds a handler for a path """
        if self.test_path(path) and self.test_path(handler):
            path_parts = self.split_path(path)                  # Splits parts into constituent components
            self.route_trie.insert(path_parts, handler)         # Passes parts on for addition to the trie

    def lookup(self, path) -> str:
        """ Lookup path and return its handler """
        if self.test_path(path):
            path_parts = self.split_path(path)                  # Splits parts into constituent components
            handler = self.route_trie.find(path_parts)          # Stores result of path search
            return handler if handler else self.path_not_found  # Returns handler if there's a match, else 404 error

    @staticmethod
    def split_path(path: str) -> List[str]:
        """ Splits path into its constituent parts """
        return [part for part in path.split('/') if part]   # Splits path at '/', handles extra slashes in the process

    @staticmethod
    def test_path(path):
        if type(path) is not str:
            print('Warning: Input path must be a string')
            exit()
        return True


router = Router("root handler", "Error 404: Page not found")    # Create a router
router.add_handler("/home/about", "about handler")              # Add a route

# Test Cases
# print(router.lookup("/"))                 # Expected: 'root handler'
# print(router.lookup("/home"))             # Expected: 'Error 404: Page not found'
# print(router.lookup("/home/about"))       # Expected: 'about handler'
# print(router.lookup("/home/about/"))      # Expected: 'about handler'
# print(router.lookup("/home/about/me"))    # Expected: 'Error 404: Page not found'
# print(router.lookup(""))                  # Expected: 'root handler'root handler
# print(router.lookup(3))                   # Expected: 'Warning: Input path must be a string'
# print(router.add_handler(3, 'handler'))   # Expected: 'Warning: Input path must be a string'
