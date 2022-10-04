from abc import ABC, abstractmethod


class IProcessor(ABC):
    @abstractmethod
    def set_next(self, processor: 'IProcessor'):
        pass

    def handle(self, data: dict):
        pass
