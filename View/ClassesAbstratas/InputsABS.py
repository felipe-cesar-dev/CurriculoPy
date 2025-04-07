from abc import abstractmethod, ABC

class InputsABC(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def input(self, camada):
        pass

    @abstractmethod
    def criarInputsDados(self, camada):
        pass

    @abstractmethod
    def criarInputsContato(self, camada):
        pass

    @abstractmethod
    def criarInputsPessoais(self, camada):
        pass

    @abstractmethod
    def criarInputsRedes(self, camada):
        pass

    @abstractmethod
    def criarInputsAdicionais(self, camada):
        pass
