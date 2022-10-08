from dataclasses import dataclass
from stat import S_IFLNK
from structured_logging.command_queue.command import Command
from structured_logging.sinks.I_sink import ISink

class LoggingCommand(Command):
    def __init__(self, sink: ISink, data:dict):
        self.sink = sink
        self.data = data

    def excecute():
        self.sink.sink_data(self.data)