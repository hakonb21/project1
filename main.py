from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.processors.enviroment_processor import EnviromentProcessor
from structured_logging.processors.null_processor import NullProcessor
from structured_logging.processors.timestamp_processor import TimestampProcessor



if __name__ == '__main__':
    env_processor = EnviromentProcessor()
    null_processor = NullProcessor()
    time_processor = TimestampProcessor()
    env_processor.set_next(null_processor)
    time_processor.set_next(env_processor)
    d = {}
    d["hallo"] = "eithvað" 
    d = time_processor.handle(d)
    console_logger = ConsoleSink()
    console_logger.sink_data(d)
    
