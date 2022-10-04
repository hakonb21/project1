from client.infrastructure.settings.settings import Settings
from structured_logging.configuration.logger_config import LoggerConfig


def create_logger_config(settings: Settings) -> LoggerConfig:
    raise NotImplementedError()
