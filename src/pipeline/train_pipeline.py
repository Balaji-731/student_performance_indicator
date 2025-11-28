import sys
from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:
    def __init__(self):
        pass

    def run_pipeline(self):
        """
        Full training workflow:
        1. Data Ingestion
        2. Data Transformation
        3. Model Training
        """
        logging.info("======== TRAINING PIPELINE STARTED ========")

        try:
            logging.info("Starting data ingestion...")
            ingestion = DataIngestion()
            train_path, test_path = ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed: Train → {train_path}, Test → {test_path}")

            logging.info("Starting data transformation...")
            transformer = DataTransformation()
            train_arr, test_arr, preprocessor_path = transformer.initiate_data_transformation(
                train_path, test_path
            )
            logging.info(f"Data transformation completed. Preprocessor saved at: {preprocessor_path}")

            logging.info("Starting model training...")
            trainer = ModelTrainer()
            best_model_name, best_score = trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(
                f"Training complete. Best Model: {best_model_name} | R2 Score: {best_score}"
            )

            logging.info("======== TRAINING PIPELINE FINISHED ========")

            return best_model_name, best_score

        except Exception as e:
            logging.exception("Error occurred in Training Pipeline")
            raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        pipeline = TrainPipeline()
        model, score = pipeline.run_pipeline()
        print(f"\nBest Model: {model}\nR2 Score: {score}")
    except Exception as e:
        print(e)
