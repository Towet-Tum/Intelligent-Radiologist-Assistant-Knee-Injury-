from IntelligentRadiologistAssistant.constants import *
from IntelligentRadiologistAssistant.utils.common import read_yaml, create_directories
from IntelligentRadiologistAssistant.entity.config_entity import DataIngestionConfig, TrainingConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def training_config(self) -> TrainingConfig:
        training = self.config.training
        params = self.params
        
        training_data = self.config.data_ingestion.unzip_dir
        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            params_epochs=params.EPOCHS,
            params_image_size=params.IMAGE_SIZE,
            training_data=Path(training_data),
        )

        return training_config
