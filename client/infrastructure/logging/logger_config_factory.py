from client.infrastructure.settings.settings import LoggingType, Settings, Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder
from structured_logging.configuration.environment import Environment as config_env


def create_logger_config(settings: Settings) -> LoggerConfig:
    logger_config_builder = LoggerConfigBuilder()
    if settings.logging_type == LoggingType.CONSOLE:
        logger_config_builder.with_console_sink()
    if settings.logging_type == LoggingType.FILE:
        logger_config_builder.with_file_sink(settings.logging_file_path)
    if settings.logging_is_async:
        logger_config_builder.as_async(settings.logging_async_delay)
    if settings.environment == Environment.DEV:
        logger_config_builder.add_environment(config_env.development)
    if settings.environment == Environment.STAGING:
        logger_config_builder.add_environment(config_env.staging)
    if settings.environment == Environment.PRODUCTION:
        logger_config_builder.add_environment(config_env.production)
    return logger_config_builder.build()