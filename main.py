from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
from networksecurity.components.data_validation import DataValidation


if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()  # ✅ Step 1: create this first
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)  # ✅ Pass it in
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info(f"initiated data ingestion")

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion completed")
        print(data_ingestion_artifact)
        data_validation_config = DataValidationConfig(training_pipeline_config=trainingpipelineconfig)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
        logging.info(f"initiated data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info(f"Data validation completed")
        print(data_validation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
