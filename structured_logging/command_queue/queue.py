from structured_logging.command_queue.command import Command
import threading
import time

from structured_logging.configuration.logger_config import LoggerConfig


class Queue:
    def __init__(self, config: LoggerConfig):
        self.async_wait_delay_in_seconds = config.async_wait_delay_in_seconds
        self.command_list = []
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()

    def add(self, command: Command):
        self.command_list.append(command)

    def __process(self):
        while True:
            if len(self.command_list) == 0:
                time.sleep(self.async_wait_delay_in_seconds)
                continue
            command = self.command_list.pop(0)
            command.execute()


            