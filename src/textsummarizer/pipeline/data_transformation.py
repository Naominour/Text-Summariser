from textsummarizer.config.configuration import Configurationmanager
from textsummarizer.components.data_transformation import DataTransformation
from textsummarizer.loggin import logger



class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configurationmanager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.convert()