import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths

    """

    # Check path path validity
    if not os.path.exists(path) or not os.access(os.path.dirname(path), os.W_OK):
        return 'Invalid path'

    # Check suffix validity
    if suffix is '' or not suffix.startswith('.') or len(suffix) < 2:
        return 'Invalid suffix'

    # Create array to store results
    files = []

    # Search directories recursively
    find_files_func(suffix, path, files)

    # Only return results if results found
    if len(files) > 0:
        return files
    else:
        return 'No files found with matching suffix'


def find_files_func(suffix, path, files):

    """ Code referenced from: https://www.devdungeon.com/content/walk-directory-python """

    path = os.path.abspath(path)

    for item in os.listdir(path):

        item_full_path = os.path.join(path, item)

        if os.path.isdir(item_full_path):
            find_files_func(suffix, item_full_path, files)

        elif item_full_path.endswith(suffix):
            files.append(item_full_path)


# Test Case 1 - expected
suffix, path = '.c', 'testdir/'

# Test Case 2 - invalid directory
# suffix, path = '.c', 'test/'

# Test Case 3 - invalid suffix
# suffix, path = '.', 'testdir/'

print(find_files(suffix, path))
