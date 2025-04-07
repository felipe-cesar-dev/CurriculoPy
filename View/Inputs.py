from tkinter.constants import CENTER
from View.ClassesAbstratas.InputsABS import InputsABC
import tkinter as tk

from View.ClassesAbstratas.LabelsABS import LabelsAbstrata


class Inputs(InputsABC):
    def __init__(self, labels: LabelsAbstrata):
        super().__init__()
        self.__labels = labels
        self.a = 0.21
        self.b = 0.47
        self.c = 0.73
        self.d = 0.5
        self.y1 = 0.11
        self.y2 = 0.37
        self.y3 = 0.63

    def input(self, camada, a, b):
        input = tk.Entry(camada, bg='light gray', font=("Arial", 14), width=15)
        input.place(relx=a, rely=b, anchor=CENTER)
        return input

    def criarInputsDados(self, camada):
        self.__labels.labelsInputs('Nome: ', camada, 0.5, self.y1, CENTER)
        self.__labels.labelsInputs('Profissão: ', camada, 0.5, self.y2, CENTER)

        nome = self.input(camada, self.d, self.a)
        profissao = self.input(camada, self.d, self.b)

    def criarInputsContato(self, camada):
        self.__labels.labelsInputs('Celular: ', camada, 0.5, self.y1, CENTER)
        self.__labels.labelsInputs('E-mail: ', camada, 0.5, self.y2, CENTER)
        self.__labels.labelsInputs('Endereço: ', camada, 0.5, self.y3, CENTER)

        celular = self.input(camada, self.d, self.a)
        email = self.input(camada, self.d, self.b)
        endereco = self.input(camada, self.d, self.c)

    def criarInputsPessoais(self, camada):
        self.__labels.labelsInputs('Data de Nascimento: ', camada, 0.5, self.y1, CENTER)
        self.__labels.labelsInputs('Estado Cívil: ', camada, 0.5, self.y2, CENTER)
        self.__labels.labelsInputs('Nacionalidade: ', camada, 0.5, self.y3, CENTER)

        nasc = self.input(camada, self.d, self.a)
        eCivil = self.input(camada, self.d, self.b)
        nacionalidade = self.input(camada, self.d, self.c)

    def criarInputsRedes(self, camada):
        self.__labels.labelsInputs('Facebook: ', camada, 0.5, self.y1, CENTER)
        self.__labels.labelsInputs('Instagram: ', camada, 0.5, self.y2, CENTER)
        self.__labels.labelsInputs('Linkedin: ', camada, 0.5, self.y3, CENTER)

        face = self.input(camada, self.d, self.a)
        insta = self.input(camada, self.d, self.b)
        linkedin = self.input(camada, self.d, self.c)

    def criarInputsAdicionais(self, camada):
        valores = {'x1': 0.5, 'y1': 0.12, 'y2': 0.28, 'y3': 0.44, 'y4': 0.60, 'y5': 0.76}
        a1 = self.input(camada, valores.get('x1'), valores.get('y1'))
        a2 = self.input(camada, valores.get('x1'), valores.get('y2'))
        a3 = self.input(camada,valores.get('x1'), valores.get('y3'))
        a4 = self.input(camada, valores.get('x1'), valores.get('y4'))
        a5 = self.input(camada, valores.get('x1'), valores.get('y5'))

    def criarInputsTexto(self, camada):
        texto = tk.Text(camada,font=("Arial", 12), height=14, width=19, bg='light gray')
        texto.place(relx=0.09, rely=0.075)

    def buildInputs(self, a, b, c, d, e, f, g, h, i):
        self.criarInputsDados(a)
        self.criarInputsContato(b)
        self.criarInputsPessoais(c)
        self.criarInputsRedes(d)
        self.criarInputsAdicionais(e)
        self.criarInputsAdicionais(f)
        self.criarInputsAdicionais(g)
        self.criarInputsAdicionais(h)
        self.criarInputsTexto(i)