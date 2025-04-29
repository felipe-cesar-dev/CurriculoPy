from Controller.ClassesAbstratas.ControleTratarDadosABS import ControleTratarDadosABS
from Model.TratarDadosABS import TratarDadosABS
from tkinter import messagebox
import re

class ControleTratarDados(ControleTratarDadosABS):
    def __init__(self, tratar: TratarDadosABS, ativacao):
        super().__init__()
        self.__tratar = tratar
        self.__ativacao = ativacao

    def salvar_nome(self, array, nome):
        array.clear()
        lenNome = nome.get()
        array.append(lenNome)
        self.__tratar.salvar_nome(array[0])
        return array.append(lenNome)

    def salvar_dados(self, nome, dado, coluna):
        colunaNome = nome[0]
        data = dado.get()
        self.__tratar.salvar_dado(colunaNome, data, coluna)

    def salvar_dado_estrangeiro(self, dado, nome, coluna, tabela):
        capturaDado = dado.get()
        pessoa_nome = nome[0]
        self.__tratar.salvar_dado_estrangeiro(capturaDado, pessoa_nome, coluna, tabela)

    def salvar_dados_lista(self, nome, coluna, dados, tabela):
        self.__tratar.salvar_dados_lista(nome, coluna, dados, tabela)

    def salvar_texto(self, dado, nome, coluna, tabela):
        capturaDado = nome[0]
        texto = dado.get(1.0, 'end')
        self.__tratar.salvar_dado_estrangeiro(texto, capturaDado, coluna, tabela)

    def verificar_nome(self, nome, entradas, textos, botoes, ativar, array, botaoNome):
        if nome.get() == "":
            messagebox.showerror("Erro", "Por favor, digite um nome válido.")
        elif not re.match("^[a-zA-ZÀ-ú ]+$", nome.get()):
            messagebox.showerror("Erro", "Por favor, digite um nome válido. Somente letras são permitidas.")
        else:
            self.salvar_nome(array, nome)
            self.__ativacao.ativar_tudo(ativar, entradas, textos)
            self.__ativacao.ativar_botoes(botoes, ativar, nome)
            botaoNome.config(state = 'disabled')
