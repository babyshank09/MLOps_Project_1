from src.MLOps_Project import logger 
from src.MLOps_Project.pipeline.data_ingestion_pipeline import DataIngestionPipeline 
from src.MLOps_Project.pipeline.data_validation_pipeline import DataValidationPipeline



if __name__ == "__main__":   
    STAGE_NAME= "Data Ingestion"
    try:
        logger.info(f"<<<<<< stage {STAGE_NAME} started >>>>>>") 
        data_ingestion = DataIngestionPipeline()
        data_ingestion.initiate_data_ingestion() 
        logger.info(f"<<<<<< stage {STAGE_NAME} completed >>>>>>")  
        
    except Exception as e: 
        logger.exception(f"stage {STAGE_NAME} failed due to {e}") 
        raise e 
        

    STAGE_NAME= "Data Validation"
    try: 
        logger.info(f"<<<<<< stage {STAGE_NAME} started >>>>>>") 
        pipeline = DataValidationPipeline() 
        pipeline.initiate_data_validation() 
        logger.info(f"<<<<<< stage {STAGE_NAME} completed >>>>>>") 
    except Exception as e: 
        logger.info(f"stage {STAGE_NAME} failed due to {e}")
        raise e
