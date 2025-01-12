import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logger import logging
from exception import CustomException
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """
    Dataclass for data ingestion configuration
    args:
        train_data_path: str: path to train data
        test_data_path: str: path to test data
        raw_data_path: str: path to raw data
    returns:
        None
    """
    train_data_path: str = os.path.join(os.getcwd(), "artifacts", "train.csv")
    test_data_path: str = os.path.join(os.getcwd(), "artifacts", "test.csv")
    raw_data_path: str = os.path.join(os.getcwd(), "artifacts", "data.csv")

class DataIngestion:
    def __init__(self, data_csv_path: str):
        self.data_csv_path = data_csv_path
        self.obj_config = DataIngestionConfig()
    
    def initiate_data_ingstion(self): 
        logging.info("Started data ingestion process")
        try:
            df = pd.read_csv(self.data_csv_path) # read raw data
            logging.info("Raw data read successfully")

            os.makedirs(os.path.dirname(self.obj_config.raw_data_path), exist_ok=True)
            df.to_csv(self.obj_config.raw_data_path, index=False, header=True) # save raw data

            logging.info("Performing train test split")
            train, test = train_test_split(df, test_size=0.2, random_state=42) # split data

            train.to_csv(self.obj_config.train_data_path, index=False, header=True)
            test.to_csv(self.obj_config.test_data_path, index=False, header=True)
            logging.info("Data ingestion process completed")

            return self.obj_config.train_data_path, self.obj_config.test_data_path

        except Exception as e:
            logging.error(CustomException(e, sys))
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    data_ingestion = DataIngestion(data_csv_path="C:\\AB_Personal\\post-hct-survival-predictions\\data\\train.csv")
    train_path, test_path = data_ingestion.initiate_data_ingstion()
    
