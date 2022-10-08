from distutils.command.config import config
import queue
from dependency_injector import containers, providers
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logger import Logger


class Container(containers.DeclarativeContainer):
    #todo: how to get settings
    config = LoggerConfig()
    q = providers.Singleton(
        Queue,
        async_wait_delay_in_seconds = config.async_wait_delay_in_seconds
        )
    
    logger = providers.Factory(
        Logger,
        logging_queue = q,
        logger_config = config
    )