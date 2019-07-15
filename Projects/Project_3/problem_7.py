from collections import defaultdict


class RouteTrieNode:
    """ Stores individual part parts along with their handlers """

    def __init__(self, handler=None):
        """ Initialises the node with children and a handler """
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, *args):
        """ Inserts a new child node """
        pass


class RouteTrie:
    """ Stores routes and associated handlers """

    def __init__(self, root_handler=None):
        """ Initialises trie with a root node and root handler """
        self.root = RouteTrieNode(root_handler)

    def insert(self, *args):
        """ Recursively adds nodes to the trie """
        # TODO: assign the handler to only the leaf (deepest) node of this path
        pass

    def find(self, *args):
        """ Finds if there is a path match """
        # TODO: Return the handler if there's a match, otherwise None
        pass


class Router:
    """ Wrapper for Trie and handles """

    def __init__(self, *args):
        """ Creates a new RouteTrie for holding routes """
        # TODO: add a handler for 404 responses
        pass

    def add_handler(self, *args):
        """ Adds a handler for a path """
        # TODO: split the path and pass parts as a list to the RouteTrie
        pass

    def lookup(self, *args):
        """ Lookup path and return its handler """
        # TODO: return None if not found or return a "not found" handler
        # TODO: Bonus - path works with/without trailing slash e.g. "/about" & "/about/" return /about handler
        pass

    @staticmethod
    def split_path(path: str):
        """ Splits path into its constituent parts """
        return [part for part in path.split('/') if part]


# create the router and add a route
router = Router("root handler", "not found handler")    # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")      # add a route

# some lookups with the expected output
print(router.lookup("/"))               # should print 'root handler'
print(router.lookup("/home"))           # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))     # should print 'about handler'
print(router.lookup("/home/about/"))    # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
