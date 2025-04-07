from View.ClassesAbstratas.BotaoABS import BotaoABS
import tkinter as tk

class Botao(BotaoABS):
    def __init__(self):
        super().__init__()

    def criarBotao(self, camada, texto, x, y, h, w):
        botao = tk.Button(text= texto, height=h, width=w, font=('Arial', 12), bg='green', fg='white')
        botao.place(in_=camada, relx=x, rely=y)
