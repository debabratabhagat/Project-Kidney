from projectKidney.config.configuration import configurationManager
from projectKidney.components.data_ingestion import DataIngestion
from projectKidney import logger


STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(config=data_ingestion_config)
        # data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> STAGE {STAGE_NAME} STARTED <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<< \n\nx=================x"
        )

    except Exception as e:
        logger.exception(e)
        raise e
