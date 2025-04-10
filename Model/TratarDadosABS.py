from abc import ABC, abstractmethod

class TratarDadosABS(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def salvar_nome(self, nome):
        pass

    @abstractmethod
    def salvar_profissao(self, nome, profissao):
        pass

    @abstractmethod
    def limparTodosDados(self):
        pass


