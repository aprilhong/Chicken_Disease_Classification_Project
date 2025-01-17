import os
import sys
import urllib.request as request
import zipfile
from ClassifierProj.logger import logging
from ClassifierProj.exception import CustomException
from ClassifierProj.utils.common import get_size
from ClassifierProj.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        try: 
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename = self.config.local_data_file
                )
                logging.info(f"{filename} download! with following info: \n{headers}")
            else:
                logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  
        except Exception as e:
            raise CustomException(e,sys)


    
    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        '''
        
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

        except Exception as e:
            raise CustomException(e,sys)