from structured_logging.command_queue.command import Command
import threading
import time


class Queue:
    def __init__(self, async_wait_delay_in_seconds):
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()
        self.async_wait_delay_in_seconds = async_wait_delay_in_seconds
        self.command_list = []

    def add(self, command: Command):
        self.command_list.append(command)

    def __process(self):
        while True:
            if self.command_list.length == 0:
                time.sleep(self.async_wait_delay_in_seconds)
                continue
            command = self.command_list.pop(0)
            command.excecute()


            