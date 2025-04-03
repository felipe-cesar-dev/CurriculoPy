from abc import abstractmethod, ABC

class InputsABC(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def input(self, camada):
        pass

    @abstractmethod
    def criarInputs(self, camada):
        pass