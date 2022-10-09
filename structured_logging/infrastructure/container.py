from dependency_injector import containers, providers
from structured_logging.command_queue.queue import Queue
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger.logger import Logger


class Container(containers.DeclarativeContainer):
    config: LoggerConfig = providers.Configuration()
    q = providers.Singleton(
        Queue,
        config = config
        )
    logger = providers.Factory(
        Logger,
        logging_queue = q,
        logger_config = config
    )