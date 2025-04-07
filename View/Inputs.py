from tkinter.constants import CENTER
from View.ClassesAbstratas.InputsABS import InputsABC
import tkinter as tk

from View.ClassesAbstratas.LabelsABS import LabelsAbstrata


class Inputs(InputsABC):
    def __init__(self, labels: LabelsAbstrata):
        super().__init__()
        self.__labels = labels
        self.a = 0.17
        self.b = 0.43
        self.c = 0.69
        self.d = 0.37
        self.y1 = 0.06
        self.y2 = 0.307
        self.y3 = 0.578

    def input(self, camada):
        input = tk.Entry(camada, bg='light gray', font=("Arial", 14), width=15)
        return input

    def criarInputsDados(self, camada):
        self.__labels.labelsInputs('Nome: ', camada, 0.14, self.y1, CENTER)
        self.__labels.labelsInputs('Profissão: ', camada, 0.18, self.y2, CENTER)

        nome = self.input(camada)
        nome.place(relx= self.d, rely= self.a, anchor=CENTER)

        profissao = self.input(camada)
        profissao.place(relx= self.d, rely= self.b, anchor=CENTER)

    def criarInputsContato(self, camada):
        self.__labels.labelsInputs('Celular: ', camada, 0.14, self.y1, CENTER)
        self.__labels.labelsInputs('E-mail: ', camada, 0.14, self.y2, CENTER)
        self.__labels.labelsInputs('Endereço: ', camada, 0.19, self.y3, CENTER)

        celular = self.input(camada)
        celular.place(relx= self.d, rely= self.a, anchor=CENTER)

        email = self.input(camada)
        email.place(relx= self.d, rely= self.b, anchor=CENTER)

        endereco = self.input(camada)
        endereco.place(relx= self.d, rely= self.c, anchor=CENTER)

    def criarInputsPessoais(self, camada):
        self.__labels.labelsInputs('Data de Nascimento: ', camada, 0.33, self.y1, CENTER)
        self.__labels.labelsInputs('Estado Cívil: ', camada, 0.21, self.y2, CENTER)
        self.__labels.labelsInputs('Nacionalidade: ', camada, 0.25, self.y3, CENTER)

        nasc = self.input(camada)
        nasc.place(relx= self.d, rely= self.a, anchor=CENTER)

        eCivil = self.input(camada)
        eCivil.place(relx= self.d, rely= self.b, anchor=CENTER)

        nacionalidade = self.input(camada)
        nacionalidade.place(relx= self.d, rely= self.c, anchor=CENTER)

    def criarInputsRedes(self, camada):
        self.__labels.labelsInputs('Facebook: ', camada, 0.19, self.y1, CENTER)
        self.__labels.labelsInputs('Instagram: ', camada, 0.19, self.y2, CENTER)
        self.__labels.labelsInputs('Linkedin: ', camada, 0.17, self.y3, CENTER)

        face = self.input(camada)
        face.place(relx= self.d, rely= self.a, anchor=CENTER)

        insta = self.input(camada)
        insta.place(relx= self.d, rely= self.b, anchor=CENTER)

        linkedin = self.input(camada)
        linkedin.place(relx= self.d, rely= self.c, anchor=CENTER)
    