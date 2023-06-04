from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def needs_service(self):
        pass


