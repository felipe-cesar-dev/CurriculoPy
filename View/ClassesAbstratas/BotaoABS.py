from abc import ABC, abstractmethod

class BotaoABS(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def criarBotao(self, camada, texto, x, y, h, w, comando):
        pass
