import os
import yaml

from box.exceptions import BoxValueError
from textsummarizer.logging import logger
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