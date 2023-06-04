from abc import abstractmethod, ABC


class Engine(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def needs_service(self):
        pass

