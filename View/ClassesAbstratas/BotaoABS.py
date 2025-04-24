from abc import ABC, abstractmethod

class BotaoABS(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def criarBotao(self, camada, texto, x, y, h, w, comando, armazenar, inputs, espacamento):
        pass

    @abstractmethod
    def criarBotaoNome(self, camada, texto, x, y, h, w, comando, armazenar):
        pass

    @abstractmethod
    def criarBotaoHTML(self, camada):
        pass
