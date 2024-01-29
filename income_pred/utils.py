import sys
import os
from income_pred.logger import logging
from income_pred.exception import CustomException
import pickle
# def save_object(file_path, obj):
#     try:
#         dir_path = os.path.dirname(file_path)

#         with open(file_path,'wb') as file_obj:
#             pickle.dump(obj,file_obj)
#     except Exception as e:
#         raise CustomException(e,sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)