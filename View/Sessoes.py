import tkinter as tk

from View.ClassesAbstratas.InputsABS import InputsABC
from View.ClassesAbstratas.SessoesABS import SessoesAbstrata

class Sessoes(SessoesAbstrata):
    def __init__(self, inputs: InputsABC):
        super().__init__()
        self.__dadosPessoais = None
        self.__infosCtt = None
        self.__infosPess = None
        self.__redes = None
        self.__cursos = None
        self.__conhecimentos = None
        self.__exp = None
        self.__formAcademica = None
        self.__sobreMim = None
        self.__inputs = inputs

    def criarSessoes(self, camada):
        self.__dadosPessoais = self.sessao(camada, 255, 227)
        self.__dadosPessoais.place(relx=0.124, rely=0.22, anchor=tk.CENTER)
        self.__inputs.criarInputsDados(self.__dadosPessoais)

        self.__infosCtt = self.sessao(camada,255, 227)
        self.__infosCtt.place(relx=0.374, rely=0.22, anchor=tk.CENTER)

        self.__infosPess = self.sessao(camada,255, 227)
        self.__infosPess.place(relx=0.624, rely=0.22, anchor=tk.CENTER)

        self.__redes = self.sessao(camada,255, 227)
        self.__redes.place(relx=0.874, rely=0.22, anchor=tk.CENTER)

        self.__cursos = self.sessao(camada,216, 342)
        self.__cursos.place(relx=0.1095, rely=0.68, anchor=tk.CENTER)

        self.__conhecimentos = self.sessao(camada,216, 342)
        self.__conhecimentos.place(relx=0.305, rely=0.68, anchor=tk.CENTER)

        self.__exp = self.sessao(camada,216, 342)
        self.__exp.place(relx=0.5, rely=0.68, anchor=tk.CENTER)

        self.__formAcademica = self.sessao(camada,216, 342)
        self.__formAcademica.place(relx=0.695, rely=0.68, anchor=tk.CENTER)

        self.__sobreMim = self.sessao(camada,216, 342)
        self.__sobreMim.place(relx=0.89, rely=0.68, anchor=tk.CENTER)

    def sessao(self, camada, w, h):
        sessao = tk.Canvas(camada, width=w, height=h, bg='#ffffff', highlightthickness=0)
        return sessao