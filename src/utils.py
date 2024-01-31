from src.logger import logging
import sys,pickle,os
from src.exception import CustomException



# if __name__ =="__main__":
#     try:
#         a = 1 / 0

#     except Exception as e:
#         logging.info('gtting error')
#         print(f'{sys} this is occured okkkkkkkkkkkkkkkkkkkkkk')
#         raise CustomException(e,sys)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok= True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)