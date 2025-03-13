from src.MLOps_Project.config.configuration import ConfigurationManager
from src.MLOps_Project.components.data_ingestion import DataIngestion 
from src.MLOps_Project.entity.config_entity import DataIngestionConfig
from src.MLOps_Project import logger 

STAGE_NAME= "Data Ingestion" 

class DataIngestionPipeline: 
    def __init__(self): 
        pass 

    def initiate_data_ingestion(self):
        try: 
            config = ConfigurationManager() 
            data_ingestion_config = config.get_data_ingestion_config() 
            data_ingestion = DataIngestion(config = data_ingestion_config)  
            data_ingestion.download_file() 
            data_ingestion.extract_zipfile() 

        except Exception as e: 
            raise e  



if __name__ == "__main__":  

    try:
        logger.info(f"<<<<<< stage {STAGE_NAME} started >>>>>>") 
        pipeline = DataIngestionPipeline()
        pipeline.initiate_data_ingestion() 
        logger.info(f"<<<<<< stage {STAGE_NAME} completed >>>>>>") 
    except Exception as e: 
        logger.exception(f"stage {STAGE_NAME} failed due to {e}") 
        raise e 




