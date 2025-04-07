import tkinter as tk

from View.ClassesAbstratas.BotaoABS import BotaoABS
from View.ClassesAbstratas.InputsABS import InputsABC
from View.ClassesAbstratas.SessoesABS import SessoesAbstrata

class Sessoes(SessoesAbstrata):
    def __init__(self, inputs: InputsABC, botao: BotaoABS):
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
        self.__botao = botao
        self.__y = 0.22
        self.__y2 = 0.68

    def criarSessoes(self, camada):
        self.__dadosPessoais = self.sessao(camada, 255, 227, 0.124, self.__y)
        self.__infosCtt = self.sessao(camada,255, 227, 0.374, self.__y)
        self.__infosPess = self.sessao(camada,255, 227, 0.624, self.__y)
        self.__redes = self.sessao(camada,255, 227, 0.874, self.__y)
        self.__cursos = self.sessao(camada,216, 342, 0.1095, self.__y2)
        self.__conhecimentos = self.sessao(camada,216, 342, 0.305, self.__y2)
        self.__exp = self.sessao(camada,216, 342, 0.5, self.__y2)
        self.__formAcademica = self.sessao(camada,216, 342, 0.695, self.__y2)
        self.__sobreMim = self.sessao(camada,216, 342, 0.89, self.__y2)

        todasSessoes = [
            self.__dadosPessoais, self.__infosCtt,  self.__infosPess, self.__redes, self.__cursos, self.__conhecimentos,
            self.__exp, self.__formAcademica, self.__sobreMim
        ]

        for i in range(len(todasSessoes)):
            self.__botao.criarBotao(todasSessoes[i], 'Salvar', 0.4, 0.85, 1, 5)

        self.__inputs.buildInputs(
            self.__dadosPessoais, self.__infosCtt, self.__infosPess, self.__redes, self.__cursos, self.__conhecimentos,
            self.__exp, self.__formAcademica, self.__sobreMim
        )

    def sessao(self, camada, w, h, x, y):
        sessao = tk.Canvas(camada, width=w, height=h, bg='#ffffff', highlightthickness=0)
        sessao.place(relx=x, rely=y, anchor=tk.CENTER)
        return sessao