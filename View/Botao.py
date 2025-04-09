from View.ClassesAbstratas.BotaoABS import BotaoABS
import tkinter as tk
from Model.ArmazenamentoABS import SQLiteDBABS

class Botao(BotaoABS):
    def __init__(self, funcao: SQLiteDBABS):
        super().__init__()
        self.__funcao = funcao

    def criarBotao(self, camada, texto, x, y, h, w, funcao):
        botao = tk.Button(text= texto, height=h, width=w, font=('Arial', 12), bg='green', fg='white')
        botao.place(in_=camada, relx=x, rely=y)
