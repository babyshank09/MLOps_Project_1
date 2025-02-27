import os 
import yaml 
from src.MLOps_Project import logger 
import joblib 
import json 
from ensure import ensure_annotations 
from typing import Any 
from box import ConfigBox 
from box.exceptions import BoxValueError 
from pathlib import Path 


@ensure_annotations 
def read_yaml_file(path_to_yaml: Path) -> ConfigBox: 

    try:
        with open(path_to_yaml) as yaml_file: 
            content = yaml.safe_load(yaml_file) 
            logger.info(f"yaml file: {path_to_yaml} loaded successfully") 
            return ConfigBox(content)

    except BoxValueError: 
        raise ValueError("yaml file is empty")   
    except Exception as e: 
        raise e


@ensure_annotations 
def create_directories(path_to_directories: list, verbose=True): 

    for path in path_to_directories: 
        os.makedirs(path, exist_ok=True) 
        if verbose: 
            logger.info(f"Created directory at {path}") 


@ensure_annotations 
def save_json(path: Path, data: dict): 
    
    with open(path, "w") as file: 
        json.dump(data, file, indent=4) 

    logger.info(f"Json file saved at {path}") 


@ensure_annotations 
def load_json(path: Path)-> ConfigBox: 
    
    with open(path) as file: 
        content= json.load(file) 

    logger.info(f"Json file loaded from path {path}") 
    return ConfigBox(content) 


@ensure_annotations 
def save_bin(data: Any, path: Path): 
    
    joblib.dump(value= data, filename= path) 
    logger.info(f"Binary file saved at {path}") 


@ensure_annotations 
def load_bin(path: Path): 
   
    data= joblib.load(path) 
    logger.info(f"Binary file loaded from {path}")  
    return data 


print("Ran successfully")