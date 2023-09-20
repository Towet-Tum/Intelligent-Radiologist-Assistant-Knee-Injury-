from IntelligentRadiologistAssistant import logger
from IntelligentRadiologistAssistant.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from IntelligentRadiologistAssistant.pipeline.stage_02_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started >>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed >>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e 


STATGE_NAME = "Training"
try:
    logger.info(f"******************************")
    logger.info(f">>>>>>>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>>>>>")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed >>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e