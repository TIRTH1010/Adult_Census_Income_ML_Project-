from src.logger import logging
import sys
from src.exception import CustomException



if __name__ =="__main__":
    try:
        a = 1 / 0

    except Exception as e:
        logging.info('gtting error')
        print(f'{sys} this is occured okkkkkkkkkkkkkkkkkkkkkk')
        raise CustomException(e,sys)