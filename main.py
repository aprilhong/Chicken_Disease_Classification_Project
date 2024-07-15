import sys
from ClassifierProj.logger import logging
from ClassifierProj.exception import CustomException

# Run to test logger.py
logging.info("Welcome to my custom classifier!")

# Run to test exception.py
try:
    a=1/0
except Exception as e:
        logging.info('Divide by Zero')
        raise CustomException(e,sys)