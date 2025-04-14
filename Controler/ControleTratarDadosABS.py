from abc import ABC, abstractmethod

class ControleTratarDadosABS(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def salvar_nome(self, array, nome):
        pass

    @abstractmethod
    def salvar_dados(self, nome, dado, coluna):
        pass

    @abstractmethod
    def salvar_rede(self, rede, nome, coluna):
        pass