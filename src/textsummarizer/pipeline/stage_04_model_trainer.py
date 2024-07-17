from textsummarizer.config.configuration import Configurationmanager
from textsummarizer.components.model_trainer import ModelTrainer
from textsummarizer.loggin import logger



class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configurationmanager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(model_trainer_config)
        model_trainer_config.train()