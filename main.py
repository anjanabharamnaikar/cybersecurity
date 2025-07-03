from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()  # ✅ Step 1: create this first
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)  # ✅ Pass it in
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info(f"initiated data ingestion")
        initiate_data_ingestion = data_ingestion.initiate_data_ingestion()
        print(initiate_data_ingestion)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
