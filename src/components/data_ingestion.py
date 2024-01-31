import os,sys
import pandas as pd 
import numpy as np 
from src.logger import logging 
from src.exception import CustomException
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('data ingestion started')
        try:
            logging.info('data reading started using pandas from local system')
            data=pd.read_csv(os.path.join('data','income_cleandata.csv'))
            logging.info('data reading sucsess')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info(f'shape of raw data is {data.shape} also head is {data.head(3)}')

            logging.info('artifacts folder created and raw data file saved sucsessfully')

            train_set,test_set=train_test_split(data,test_size=0.30,random_state=42)

            logging.info(f'shape of train data is {train_set.shape} head is {train_set.head(3)} and test data is {test_set.shape} and head is {test_set.head(3)}')


            logging.info('train and test is seprated')

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('data ingestion completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info('error occure in data ingestion state')
            raise CustomException(e,sys)
        

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path , test_data_path =obj.initiate_data_ingestion()


    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.inititate_data_transformation(train_data_path , test_data_path)




