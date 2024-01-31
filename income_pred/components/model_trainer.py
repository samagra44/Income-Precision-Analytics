import os
import sys
import pandas as pd
import numpy as np
from income_pred.logger import logging
from income_pred.exception import CustomException
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from income_pred.utils import save_object
from income_pred.utils import evaluate_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

@dataclass
class ModelTrainingConfig:
    train_model_file_path = os.path.join("artifacts/model_trainer","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainingConfig()
    
    def initiate_model_trainer(self, train_array,test_array):
        try:
            logging.info("Splitting the data into Independent and Dependent Features")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            model = {
                "RandomForest Classifier":RandomForestClassifier(),
                "Decision Tree Classifier":DecisionTreeClassifier(),
                "Logistic Regression":LogisticRegression()
            }
            params = {
                "RandomForest Classifier":{
                    "class_weight":['balanced'],
                    'n_estimators':[20,50,30],
                    'max_depth':[10,8,5],
                    'min_samples_split':[2,5,10],
                },
                "Decision Tree Classifier":{
                    "class_weight":['balanced'],
                    'criterion':['gini','entropy','log_loss'],
                    'splitter':['best', 'random'],
                    'max_depth':[3,4,5,6],
                    'min_samples_split':[2,3,4,5],
                    'min_samples_leaf':[1,2,3],
                    'max_features':['auto','sqrt','log2']
                },
                "Logistic Regression":{
                    'class_weight':['balanced'],
                    'penalty':['l1','l2'],
                    'C':[0.001, 0.01, 0.1, 10, 100],
                    'solver':['liblinear','saga']
                }
            }

            model_report:dict = evaluate_model(X_train = X_train, y_train = y_train, X_test = X_test, y_test =y_test,
                                                models = model, params = params)

            # getting the best model
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = model[best_model_name]
            print(f"Best Model Found: {best_model_name}, with accuracy {best_model_score}")
            print("***********************************************************************")
            logging.info("Best Model Found: {best_model_name}, with accuracy {best_model_score}")

            save_object(file_path=self.model_trainer_config.train_model_file_path,obj=best_model)
        except Exception as e:
            raise CustomException(e,sys)
