from abc import ABC, abstractmethod

class ControleBotoesABS(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def botaoclicado(self, botao, inputs, botaoeditar):
        pass

    @abstractmethod
    def botaoclicadoEditar(self, botao, inputs, botaoeditar):
        pass
