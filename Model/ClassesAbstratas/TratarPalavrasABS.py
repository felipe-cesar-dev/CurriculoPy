from abc import abstractmethod, ABC

class ControleLengthABS(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def verificarNome(self, palavra):
        pass