from abc import ABC, abstractmethod

class ControleTratarDadosABS(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def salvar_dados(self, array, nome):
        pass
