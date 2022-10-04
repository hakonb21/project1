from structured_logging.processors.abstract_processor import AbstractProcessor
from structured_logging.configuration.environment import Environment

class EnviromentProcessor(AbstractProcessor):
    def __init__(self, enviroment):
        self.enviroment = enviroment

    def handle(self, data: dict):
        data["enviroment"] = self.enviroment
        return super().handle(data)