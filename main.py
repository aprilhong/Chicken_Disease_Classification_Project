import sys
from ClassifierProj.logger import logging
from ClassifierProj.exception import CustomException
from ClassifierProj.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# # Run to test logger.py
# logging.info("Welcome to my custom classifier!")

# # Run to test exception.py
# try:
#     a=1/0
# except Exception as e:
#         logging.info('Divide by Zero')
#         raise CustomException(e,sys)



# Run DataIngestionTrainingPipeline
STAGE_NAME = "Data Ingestion Stage"
if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            raise CustomException(e,sys)