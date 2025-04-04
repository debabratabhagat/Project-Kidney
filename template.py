import os
from pathlib import Path
import logging

"""logging string"""
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] - %(message)s")

project_name = "Project-Kidney"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "reasearch/trials.ipynb",
    "templates/index.html",
    "test.py",
]

for filepath in list_of_files:
    filepath = Path(
        filepath
    )  # convert to path object; helps convert to os specific path independent of '/' or '\'
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory : {filedir} created")

    if (not os.path.exists(filepath)) or (os.path.getsize(filename=filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"File: {filename} created")

    else:
        logging.info(f"{filename} exists")
