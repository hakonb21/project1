from imp import NullImporter
from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.I_processor import IProcessor
from structured_logging.sinks.I_sink import ISink
from structured_logging.sinks.file_sink import FileSink
from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.processors.null_processor import NullProcessor


class LoggerConfigBuilder:
    def __init__(self):
        self.sink = ConsoleSink()
        self.processor = NullProcessor()
        self.is_async = False
        self.async_wait_delay_in_seconds = 0
        self.environment = None

    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        self.sink = sink
        return self

    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        self.sink = FileSink(file_path)
        return self

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        self.sink = ConsoleSink()
        return self

    def as_async(self, wait_delay_in_seconds: int) -> 'LoggerConfigBuilder':
        self.is_async = True
        self.async_wait_delay_in_seconds = wait_delay_in_seconds
        return self

    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        self.environment = environment
        return self

    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        self.processor = processor
        return self

    def _clear(self):
        self.sink = ConsoleSink()
        self.processor = NullProcessor()
        self.is_async = False
        self.async_wait_delay_in_seconds = 0
        return self

    def build(self) -> LoggerConfig:
        return LoggerConfig(
            sink = self.sink,
            processor = self.processor, 
            is_async = self.is_async, 
            async_wait_delay_in_seconds = self.async_wait_delay_in_seconds,
            environment = self.environment
            )
