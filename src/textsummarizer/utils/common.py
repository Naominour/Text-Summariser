import os
import yaml

from box.exceptions import BoxValueError
from textsummarizer.loggin import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns

    Args:
         path_to_yaml (Path): Path to the yaml file to be read
    Raises:
         BoxValueError: If the yaml file does not exist
    Returns:
          ConfigBox: A box containing the contents of the yaml file
 

    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories
        
    Args:
        path_to_directories (list): A list of directories to be created
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
           logger.info(f"Created directory: {path}")


@ensure_annotations
def get_size(path: Path) -> str:

    """
    Get size in KB

    Args:
        path (Path): Path to the file whose size is to be found

    Returns the size of a file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"