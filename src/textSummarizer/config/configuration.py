from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml,create_directories
from textSummarizer.entity import (DataIngestionConfig)
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
        print(config_filepath)
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        print(self.config)
        create_directories([self.config.atrifacts_root])
        print("This is the exception")
    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        print(data_ingestion_config)

        return data_ingestion_config