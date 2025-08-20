from textsummarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.data_transformation import DataTransformationTrainingPipeline
from textsummarizer.pipeline.model_trainer import ModelTrainerTrainingPipeline
from textsummarizer.pipeline.model_evaluation import ModelEvaluationTrainingPipeline
from textsummarizer.loggin import logger



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<")
    model_trainer = ModelEvaluationTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e