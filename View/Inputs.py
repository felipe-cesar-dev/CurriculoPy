from tkinter.constants import CENTER
from View.ClassesAbstratas.InputsABS import InputsABC
import tkinter as tk

from View.ClassesAbstratas.LabelsABS import LabelsAbstrata


class Inputs(InputsABC):
    def __init__(self, labels: LabelsAbstrata):
        super().__init__()
        self.__labels = labels

    def input(self, camada):
        input = tk.Entry(camada, bg='light gray', font=("Arial", 14), width=15)
        return input

    def criarInputsDados(self, camada):
        self.__labels.labelsInputs('Nome: ', camada, 0.14, 0.20, CENTER)
        self.__labels.labelsInputs('Profissão: ', camada, 0.18, 0.50, CENTER)
        nome = self.input(camada)
        nome.place(relx= 0.37, rely= 0.35, anchor=CENTER)
        profissao = self.input(camada)
        profissao.place(relx= 0.37, rely= 0.65, anchor=CENTER)

    def criarInputsContato(self, camada):
        self.__labels.labelsInputs('Celular: ', camada, 0.14, 0.12, CENTER)
        self.__labels.labelsInputs('E-mail: ', camada, 0.14, 0.42, CENTER)
        self.__labels.labelsInputs('Endereço: ', camada, 0.20, 0.72, CENTER)

        celular = self.input(camada)
        celular.place(relx= 0.37, rely= 0.27, anchor=CENTER)

        email = self.input(camada)
        email.place(relx= 0.37, rely= 0.57, anchor=CENTER)

        endereco = self.input(camada)
        endereco.place(relx= 0.37, rely= 0.87, anchor=CENTER)
    