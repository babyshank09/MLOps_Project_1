from src.MLOps_Project.constants import * 
from src.MLOps_Project.utils.common import read_yaml_file, create_directories
import yaml 
from src.MLOps_Project.entity.config_entity import (DataIngestionConfig, DataValidationConfig)


class ConfigurationManager: 
    def __init__(
    self, 
    config_filepath = CONFIG_FILE_PATH, 
    schema_filepath= SCHEMA_FILE_PATH, 
    params_filepath= PARAMS_FILE_PATH
    ): 
        self.config_filepath = read_yaml_file(config_filepath)
        self.schema_filepath = read_yaml_file(schema_filepath)
        self.params_filepath = read_yaml_file(params_filepath)  

        create_directories([self.config_filepath.artifacts_root])  


    def get_data_ingestion_config(self)-> DataIngestionConfig: 
        
        config = self.config_filepath.data_ingestion 
        create_directories([config.root_dir])

        data_ingestion_config= DataIngestionConfig(
            root_dir = Path(config.root_dir), 
            source_URL = str(config.source_URL), 
            local_data_file = Path(config.local_data_file), 
            unzip_dir = Path(config.unzip_dir)
        )  

        return data_ingestion_config 

    
    def get_data_validation_config(self)->DataValidationConfig:  

        config = self.config_filepath.data_validation 
        schema = self.schema_filepath.COLUMNS 

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir, 
            unzip_dir = config.unzip_dir, 
            STATUS_FILE = config.STATUS_FILE, 
            all_schema = schema
        ) 

        return data_validation_config

