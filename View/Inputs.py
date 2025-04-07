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

    def criarInputsContato(self, camada):
        celularLabel = tk.Label(camada, text='Celular: ', font=('Arial', 12), bg='white')
        celularLabel.place(relx= 0.14, rely= 0.12, anchor=CENTER)
        celular = self.input(camada)
        celular.place(relx= 0.37, rely= 0.27, anchor=CENTER)

        emailLabel = tk.Label(camada, text='Profissão: ', font=('Arial', 12), bg='white')
        emailLabel.place(relx= 0.18, rely= 0.42, anchor=CENTER)
        email = self.input(camada)
        email.place(relx= 0.37, rely= 0.57, anchor=CENTER)

        enderecoLabel = tk.Label(camada, text='Endereço: ', font=('Arial', 12), bg='white')
        enderecoLabel.place(relx= 0.20, rely= 0.72, anchor=CENTER)
        endereco = self.input(camada)
        endereco.place(relx= 0.37, rely= 0.87, anchor=CENTER)
    