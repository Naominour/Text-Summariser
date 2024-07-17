from textsummarizer.config.configuration import Configurationmanager
from textsummarizer.components.data_ingestion import DataIngestion
from textsummarizer.loggin import logger



class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configurationmanager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
