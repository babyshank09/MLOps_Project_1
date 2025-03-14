from src.MLOps_Project.config.configuration import ConfigurationManager 
from src.MLOps_Project.components.data_validation import DataValidation 
from src.MLOps_Project.entity.config_entity import DataValidationConfig 
from src.MLOps_Project import logger 

STAGE_NAME = "Data Validation" 

class DataValidationPipeline(): 
    def __init__(self): 
        pass 

    def initiate_data_validation(self): 
        try: 
            config = ConfigurationManager() 
            data_validation_config = config.get_data_validation_config() 
            data_validation = DataValidation(config = data_validation_config) 
            data_validation.validate_all_columns() 

        except Exception as e: 
            raise e 

if __name__ == "__main__": 
    try: 
        logger.info(f"<<<<<< stage {STAGE_NAME} started >>>>>>") 
        pipeline = DataValidationPipeline() 
        pipeline.initiate_data_validation() 
        logger.info(f"<<<<<< stage {STAGE_NAME} completed >>>>>>") 
    except Exception as e: 
        logger.info(f"stage {STAGE_NAME} failed due to {e}")
        raise e