from structured_logging.processors.abstract_processor import AbstractProcessor
from datetime import datetime


class TimestampProcessor(AbstractProcessor):
    def handle(self, data: dict):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data["timestamp"] = current_time
        return super().handle(data)
