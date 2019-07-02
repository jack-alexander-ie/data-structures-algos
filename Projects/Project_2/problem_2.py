import os


def find_files(suffix, path):

    # Check path path validity
    if not os.path.exists(path) or not os.access(os.path.dirname(path), os.W_OK):
        return 'Invalid path'

    # Check suffix validity
    if suffix is '' or not suffix.startswith('.') or len(suffix) < 2:
        return 'Invalid suffix'

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


# Test Case 1 - expected
suffix, path = '.c', 'testdir/'

# Test Case 2 - invalid directory
# suffix, path = '.c', 'test/'

# Test Case 3 - invalid suffix
# suffix, path = '.', 'testdir/'

print(find_files(suffix, path))
