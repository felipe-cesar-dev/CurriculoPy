from tkinter.constants import CENTER
from View.ClassesAbstratas.InputsABS import InputsABC
import tkinter as tk

class Inputs(InputsABC):
    def __init__(self):
        super().__init__()

    def input(self, camada):
        input = tk.Entry(camada, bg='light gray', font=("Arial", 14), width=15)
        return input

    def criarInputsDados(self, camada):
        nomeLabel = tk.Label(camada, text='Nome: ', font=('Arial', 12), bg='white')
        nomeLabel.place(relx= 0.14, rely= 0.20, anchor=CENTER)
        nome = self.input(camada)
        nome.place(relx= 0.37, rely= 0.35, anchor=CENTER)
        profissaLabel = tk.Label(camada, text='Profissão: ', font=('Arial', 12), bg='white')
        profissaLabel.place(relx= 0.18, rely= 0.50, anchor=CENTER)
        profissao = self.input(camada)
        profissao.place(relx= 0.37, rely= 0.65, anchor=CENTER)