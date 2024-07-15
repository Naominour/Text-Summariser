from textsummarizer.config.configuration import Configurationmanager
from textsummarizer.components.data_transformation import ModelEvaluation
from textsummarizer.loggin import logger



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configurationmanager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.evaluate()