import os

# Base directory is the root of the project (containing Database and Data_Storage folders)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_path(relative_path):
    return os.path.join(BASE_DIR, relative_path)
