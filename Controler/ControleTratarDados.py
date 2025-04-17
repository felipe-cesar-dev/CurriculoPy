from Controler.ControleTratarDadosABS import ControleTratarDadosABS
from Model.TratarDadosABS import TratarDadosABS
import sqlite3 as sq

class ControleTratarDados(ControleTratarDadosABS):
    def __init__(self, tratar: TratarDadosABS):
        super().__init__()
        self.__tratar = tratar

    def salvar_nome(self, array, nome):
        array.clear()
        array.append(nome.get())
        print(array)
        self.__tratar.salvar_nome(array[0])
        return array.append(nome.get())

    def salvar_dados(self, nome, dado, coluna):
        colunaNome = nome[0]
        data = dado.get()
        self.__tratar.salvar_dado(colunaNome, data, coluna)

    def salvar_dado_estrangeiro(self, dado, nome, coluna, tabela):
        capturaRede = dado.get()
        pessoa_nome = nome[0]
        self.__tratar.salvar_dado_estrangeiro(capturaRede, pessoa_nome, coluna, tabela)

    def salvar_dados_lista(self, nome, coluna, dados, tabela):
        self.__tratar.salvar_dados_lista(nome, coluna, dados, tabela)
