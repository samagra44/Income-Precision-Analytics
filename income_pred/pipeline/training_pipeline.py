import os
import sys
from income_pred.logger import logging
from income_pred.exception import CustomException
from income_pred.components.data_ingestion import DataIngestion
from income_pred.components.data_transformation import DataTransformation
from income_pred.components.model_trainer import ModelTrainer
from dataclasses import dataclass

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    data_tranformation  = DataTransformation()
    train_arr, test_arr, _ = data_tranformation.inititate_data_transformation(train_data_path,test_data_path)
    model_training = ModelTrainer()
    model_training.initiate_model_trainer(train_arr, test_arr) 