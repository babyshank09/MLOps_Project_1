import os 
from pathlib import Path  
import logging 


project_name= "MLOps_Project"  


logging.basicConfig(
    level= logging.INFO,
    format= '[%(asctime)s]: %(message)s:',
    handlers=[ 
        logging.StreamHandler()
    ]
)


file_names= [ 
    ".github/workflows/.gitkeep", 
    f"src/{project_name}/__init__.py",  
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py",   
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py", 
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/entity/config_entity.py", 
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml", 
    "params.yaml", 
    "schema.yaml",
    "main.py", 
    "Dockerfile", 
    "requirements.txt", 
    "setup.py", 
    "research.ipynb", 
    "templates/index.html", 
    "app.py"
]



for filepath in file_names: 
    filepath= Path(filepath)
    filedir, filename= os.path.split(filepath)
    

    if os.path.exists(filepath):  
        logging.info(f"{filepath} in already exists")  
    

    else:

        if os.path.exists(filedir) or filedir=="":  
            print(filepath)
            with open(filepath, "w") as file: 
                
                pass  
                logging.info(f"Creating empty file {filepath}")    


        else: 
            os.makedirs(filedir, exist_ok=True) 
            logging.info(f"Creating directory {filedir} for the file {filename}")  

            with open(filepath, "w") as file: 
                
                pass  
                logging.info(f"Creating empty file {filepath}")    

        

 





        
    


