from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.I_processor import IProcessor
from structured_logging.sinks.I_sink import ISink
from structured_logging.sinks.file_sink import FileSink
from structured_logging.sinks.console_sink import ConsoleSink


class LoggerConfigBuilder:
    def __init__(self):
        self.logger_cf = LoggerConfig()

    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        self.logger_cf.sink = sink
        return self.logger_cf

    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        self.logger_cf.sink = FileSink(file_path)
        return self.logger_cf

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        self.logger_cf.sink = ConsoleSink()
        return self.logger_cf

    def as_async(self, wait_delay_in_seconds: int) -> 'LoggerConfigBuilder':
        self.logger_cf.is_async = True
        self.logger_cf.async_wait_delay_in_seconds = wait_delay_in_seconds
        return self.logger_cf

    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        raise NotImplementedError()

    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        raise NotImplementedError()

    def _clear(self):
        raise NotImplementedError()

    def build(self) -> LoggerConfig:
        raise NotImplementedError()
