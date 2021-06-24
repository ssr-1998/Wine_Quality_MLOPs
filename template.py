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
