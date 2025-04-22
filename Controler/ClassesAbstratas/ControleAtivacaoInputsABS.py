from abc import ABC, abstractmethod

class ControleAtivacaoInputsABS(ABC):
    def __init__(self):
        pass

    def ativar_tudo(self, ativar, entradas, textos):
        pass

    def __atualizar_estados(self, entradas, ativar, textos):
        pass

    def ativar_botoes(self, botoes, ativar, nome):
        pass

    def atualizar_botoes(self, botoes, ativar, nome):
        pass