import pandas as pd  
from src.MLOps_Project import logger  
import os 
from src.MLOps_Project.entity.config_entity import DataValidationConfig

class DataValidation(): 
    def __init__(self, config:DataValidationConfig): 
        self.config = config  


    def validate_all_columns(self)-> bool:
        try: 
            validation = None

            data = pd.read_csv(self.config.unzip_dir)  
            columns = list(data.columns)   

            schema_cols = list(self.config.all_schema.keys())
            

            for col in columns: 
                if col not in schema_cols:  
                    validation = False 
                    with open(self.config.STATUS_FILE, "w") as file: 
                        file.write(f"{col}: {validation}")   
                    break

                else:  
                    validation = True 
                    with open(self.config.STATUS_FILE, "w") as file: 
                        file.write(f"{col}: {validation}")    
                

            return validation 

        except Exception as e: 
            raise e  
