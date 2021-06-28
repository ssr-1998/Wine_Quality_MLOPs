import os

# Making Some Directories & Files for Project.

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)  # exist_ok is set to True so that if directory is already there, it won't throw any error.
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]

for file_ in files:
    with open(file_, "w") as g:
        pass


# from setuptools import setup, find_packages
# # In this way, one can make a package. Just like numpy, pandas are packages.
# # To make this a package. Run "pip install -e ." this command will install all the packages avaialable
# # in local directory.

# # Benefit of doing this is that now anywhere on my system I can import src package & use any of its file.

# setup(
#     name="src",
#     version="0.0.1",
#     description="It's a Wine Quality Package",
#     author="ssr-1998",
#     packages=find_packages(),
#     license="MIT"
# )

