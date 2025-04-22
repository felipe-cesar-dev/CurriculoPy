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
    def salvar_dados_lista(self, nome, coluna, dados, tabela):
        pass

    @abstractmethod
    def salvar_dado_estrangeiro(self, dado, nome, coluna, tabela):
        pass

    @abstractmethod
    def salvar_texto(self, dado, nome, coluna, tabela):
        pass

    @abstractmethod
    def verificar_nome(self, nome, entradas, textos, botoes, ativar, array, botaoNome):
        pass