from typing import Any, Iterable
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logging_command import LoggingCommand


class Logger:
    def __init__(self, logger_config: LoggerConfig, logging_queue: Queue):
        self.__logger_config = logger_config
        self.__logging_queue = logging_queue

    def log(self, **kwargs: Iterable[Any]):
        data = self.__logger_config.processor.handle(kwargs)
        logging_command = LoggingCommand(self.__logger_config.sink, data)
        if self.__logger_config.is_async:
            self.__logging_queue.add(logging_command)
        else:
            logging_command.excecute()
        