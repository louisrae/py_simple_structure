import os

from .constants import *
from .utils import *


def create_file_structure(project_name):
    os.chdir(os.path.expanduser(("~/Documents")))
    source_folder_name = project_name.lower()
    templates_path = (
        "/Users/louisrae/Documents/dev/project_structures/project_structures"
    )

    top_level_project_path = f"dev/{project_name}"
    source_dir_path = f"{top_level_project_path}/{source_folder_name}"
    test_dir_path = f"{top_level_project_path}/tests"

    app_path = f"{source_dir_path}/app.py"
    utils_path = f"{source_dir_path}/utils.py"
    constants_path = f"{source_dir_path}/constants.py"
    test_app_path = f"{test_dir_path}/test_app.py"

    # Create folder structure
    os.mkdir(top_level_project_path)
    os.mkdir(source_dir_path)
    os.mkdir(test_dir_path)

    # Create init files for packages
    open(f"{source_dir_path}/__init__.py", "w")
    open(f"{test_dir_path}/__init__.py", "w")

    # Create main file for writing code
    with open(app_path, "w") as f:
        f.write("from .constants import *")
        f.write("\n")
        f.write("from .utils import *")

    # Create sub files for code organization
    open(utils_path, "w")
    open(constants_path, "w")

    # Create test file for main file
    with open(test_app_path, "w") as f:
        f.write(f"from {source_folder_name} import app")

    # Create README

    with open(f"{top_level_project_path}/README.md", "w") as f:
        with open(f"{templates_path}/README_global.md", "r") as f1:
            for line in f1:
                f.write(line)

    # Create .gitignore
    with open(f"{top_level_project_path}/.gitignore", "w") as f:
        with open(f"{templates_path}/.gitignore_global", "r") as f1:
            for line in f1:
                f.write(line)

    # Create file to run code from
    with open(f"{top_level_project_path}/main.py", "w") as f:
        f.write(f"from {source_folder_name}  import app")

    # Create file to hold important variable (included in gitignore)
    open(f"{top_level_project_path}/.env", "w")
