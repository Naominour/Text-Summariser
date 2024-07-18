import os
import logging

from pathlib import Path


logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s')


project_name = "textsummarizer"

list_of_files = [
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/loggin/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepaths in list_of_files:
    filepaths = Path(filepaths)
    filedir, filename = os.path.split(filepaths)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")


    if (not os.path.exists(filepaths)) or (os.path.getsize(filepaths) == 0):
        with open(filepaths, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepaths}")

    else:
        logging.info(f"{filepaths} IS already exists")


