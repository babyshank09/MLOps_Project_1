import os 
import urllib.request as request 
from src.MLOps_Project import logger 
import zipfile  
from src.MLOps_Project.entity.config_entity import (DataIngestionConfig)



class DataIngestion:  
    def __init__(self, config: DataIngestionConfig): 
        self.config = config 


    def download_file(self): 
        if not os.path.exists(self.config.local_data_file): 
            filename, headers = request.urlretrieve(
                url= self.config.source_URL, 
                filename = self.config.local_data_file
            ) 

            logger.info(f"{filename} downloaded! with the following info {headers}") 

        else: 
            logger.info("File already exists") 

    
    def extract_zipfile(self): 
        unzip_path = self.config.unzip_dir 
        os.makedirs(unzip_path, exist_ok = True) 
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref: 
            zip_ref.extractall(unzip_path)  

        logger.info(f"{self.config.local_data_file} unziped at {unzip_path}")

    