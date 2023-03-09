import logging
import sys
import os
from  datetime import datetime
from exception import CustomExcpetion

current_time= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE=f"log_{current_time}.log"
logs_path= os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s",
    level=logging.INFO
)