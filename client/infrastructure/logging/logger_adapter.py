from client.infrastructure.logging.I_logger import ILogger
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logger import Logger


class LoggerAdapter(ILogger):
    def __init__(self, external_logger: Logger):
        self.external_logger = external_logger
        
    def error(self, message: str, exception: Exception = None):
        d = {}
        d["message"] = message
        d["exception"] = exception
        d["message type"] = "error"
        self.external_logger.log(**d)

    def warning(self, message: str, exception: Exception = None):
        d = {}
        d["message"] = message
        d["exception"] = exception
        d["message type"] = "warning"
        self.external_logger.log(**d)

    def info(self, message: str):
        d = {}
        d["message"] = message
        d["message type"] = "info"
        self.external_logger.log(**d)
