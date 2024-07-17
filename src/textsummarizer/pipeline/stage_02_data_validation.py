from textsummarizer.config.configuration import Configurationmanager
from textsummarizer.components.data_validation import DataValidation
from textsummarizer.loggin import logger



class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configurationmanager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exist()
