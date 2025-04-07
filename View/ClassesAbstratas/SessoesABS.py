from abc import abstractmethod, ABC


class SessoesAbstrata(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def criarSessoes(self, camada):
        pass
    @abstractmethod
    def sessao(self, camada, w, h, x, y):
        pass