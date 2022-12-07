import argparse

from project_structures import app

parser = argparse.ArgumentParser(description="project creation")
parser.add_argument("-n", "--name", help="name of the project", required=True)
args = vars(parser.parse_args())


app.create_file_structure(args["name"])
