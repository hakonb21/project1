from structured_logging.processors.abstract_processor import AbstractProcessor
from structured_logging.configuration.environment import Environment

class EnviromentProcessor(AbstractProcessor):
    def handle(self, data: dict):
        data["enviroment"] = Environment.staging.value
        return super().handle(data)