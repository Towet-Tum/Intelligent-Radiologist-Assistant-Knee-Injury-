from dataclasses import dataclass, astuple
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path 



@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    training_data: Path
    params_epochs: int 
    params_image_size: int 
    
    def __iter__(self):
        return iter(astuple(self))