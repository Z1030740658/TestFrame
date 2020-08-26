import os


def find_project_root():
    """
    Searches conftest.py file in current or parent directories
    :return string of absolute normal path to conftest file (including file)
    :raise NameError if file was not found
    """
    folder = os.getcwd()
    file_name = "conftest.py"

    while folder != os.path.dirname(folder):
        files = os.listdir(folder)
        if file_name in files:
            return folder
        folder = os.path.normpath(os.path.join(folder, os.pardir))

    raise NameError("No '{}' config file found".format(file_name))


PROJECT_PATH = find_project_root()
