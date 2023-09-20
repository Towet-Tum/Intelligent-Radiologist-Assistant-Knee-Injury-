from IntelligentRadiologistAssistant.config.configuration import ConfigurationManager
from IntelligentRadiologistAssistant.components.training import Training
from IntelligentRadiologistAssistant import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self) -> None:
         pass 
    
    def main(self):
        training = Training()
        training.model_train_val()


if __name__ == '__main__':
    try:
        logger.info(f"*********************************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e