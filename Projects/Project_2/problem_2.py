import os


def validity_checker(suffix: str, path: str) -> tuple:
    # Check path path validity
    if not os.path.exists(path) or not os.access(os.path.dirname(path), os.W_OK):
        return False, 'The path given is invalid'
    # Check suffix validity
    if suffix is '' or not suffix.startswith('.') or len(suffix) < 2:
        return False, 'The suffix given is invalid'
    return True, None


def find_files(suffix: str, path: str):

    # Check path and suffix validity
    validity, message = validity_checker(suffix, path)
    if not validity:
        return message

    # Create array to store results
    files = []

    # Search directories recursively
    def find_files_rec(suffix, path, files):
        """ Code referenced from: https://www.devdungeon.com/content/walk-directory-python """
        path = os.path.abspath(path)
        for item in os.listdir(path):
            item_full_path = os.path.join(path, item)
            if os.path.isdir(item_full_path):
                find_files_rec(suffix, item_full_path, files)
            elif item_full_path.endswith(suffix):
                files.append(item_full_path)
    find_files_rec(suffix, path, files)
    # Only return results if results found
    if len(files) > 0:
        return files
    else:
        return 'No files found with matching suffix'


# Test Case 1 - Expected
suffix, path = '.c', 'testdir/'
"""
Expected Output: 

['.../testdir/subdir1/a.c', '.../testdir/subdir5/a.c', '.../testdir/t1.c', '.../testdir/subdir3/subsubdir1/b.c']
"""

# Test Case 2 - Invalid directory
# suffix, path = '.c', 'test/'
"""
Expected Output: 'The path given is invalid'
"""

# Test Case 3 - Invalid suffix
# suffix, path = '.', 'testdir/'
"""
Expected Output: 'The suffix given is invalid'
"""

print(find_files(suffix, path))
