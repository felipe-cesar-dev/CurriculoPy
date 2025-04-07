from View.ClassesAbstratas.BotaoABS import BotaoABS
import tkinter as tk

class BotaoArmazenar(BotaoABS):
    def __init__(self):
        super().__init__()

    def criarBotao(self, camada):
        botao = tk.Button(text= 'Salvar', height=1, width=5, font=('Arial', 12), bg='green', fg='white')
        botao.place(in_=camada, relx=0.4, rely=0.85)
