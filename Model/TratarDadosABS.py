from abc import ABC, abstractmethod

class TratarDadosABS(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def salvar_nome(self, nome):
        pass

    @abstractmethod
    def salvar_dado(self, nome, dado, coluna):
        pass

    @abstractmethod
    def salvar_dado_estrangeiro(self, dado, nome, coluna, tabela):
        pass

    @abstractmethod
    def salvar_dados_lista(self, nome, coluna, dados, tabela):
        pass

    @abstractmethod
    def limparTodosDados(self):
        pass



