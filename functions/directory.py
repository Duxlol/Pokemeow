import os

directory = "items"

parent_dir = "./"

path = os.path.join(parent_dir, directory)

def mkdir():
    os.mkdir(path)