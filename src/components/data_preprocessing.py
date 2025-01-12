import os
import json
import sys
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logger import logging
from exception import CustomException
from dataclasses import dataclass
import pickle

# creating the preprocessor object
@dataclass
class DataPreprocessingConfig:
    """
    Dataclass for data preprocessing configuration
    args:
        train_data_path: str: path to train data
        test_data_path: str: path to test data
        raw_data_path: str: path to raw data
        preprocessed_data_path: str: path to preprocessed data
    returns:
        None
    """
    train_data_path: str = os.path.join(os.getcwd(), "artifacts", "train.csv")
    test_data_path: str = os.path.join(os.getcwd(), "artifacts", "test.csv")
    raw_data_path: str = os.path.join(os.getcwd(), "artifacts", "data.csv")
    preprocessed_data_path: str = os.path.join(os.getcwd(), "artifacts", "preprocessed_data.csv")
    preprocessor_obj_file_path = os.path.join(os.getcwd(), "artifacts", "preprocessor_obj.pkl")
