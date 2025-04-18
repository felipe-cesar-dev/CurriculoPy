from tkinter.constants import CENTER
from Controler.ControleTratarDadosABS import ControleTratarDadosABS
from View.ClassesAbstratas.BotaoABS import BotaoABS
from View.ClassesAbstratas.InputsABS import InputsABC
import tkinter as tk
from View.ClassesAbstratas.LabelsABS import LabelsAbstrata

class Inputs(InputsABC):
    def __init__(self, labels: LabelsAbstrata, tratar: ControleTratarDadosABS, botao: BotaoABS):
        super().__init__()
        self.__labels = labels
        self.__nome = []
        self.__tratar = tratar
        self.__botao = botao
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
        self.__labels.labelsInputs('Nome: ', camada, self.d, self.y1, CENTER)
        self.__labels.labelsInputs('Profissão: ', camada, self.d, self.y2, CENTER)
        nome = self.input(camada, self.d, self.a)
        profissao = self.input(camada, self.d, self.b)
        self.__botao.criarBotao(
            camada, 'Salvar', 0.4, 0.83, 1, 5, lambda: [
                self.__tratar.salvar_nome(self.__nome, nome),
                self.__tratar.salvar_dados(self.__nome, profissao,'Profissao')
            ]
        )

    def criarInputsContato(self, camada):
        self.__labels.labelsInputs('Celular: ', camada, self.d, self.y1, CENTER)
        self.__labels.labelsInputs('E-mail: ', camada, self.d, self.y2, CENTER)
        self.__labels.labelsInputs('Endereço: ', camada, self.d, self.y3, CENTER)

        celular = self.input(camada, self.d, self.a)
        email = self.input(camada, self.d, self.b)
        endereco = self.input(camada, self.d, self.c)
        self.__botao.criarBotao(
            camada, 'Salvar', 0.4, 0.83, 1, 5, lambda: [
                self.__tratar.salvar_dados(self.__nome, celular, 'Celular'),
                self.__tratar.salvar_dados(self.__nome, email, 'Email'),
                self.__tratar.salvar_dados(self.__nome, endereco, 'Endereco')
            ]
        )

    def criarInputsPessoais(self, camada):
        self.__labels.labelsInputs('Data de Nascimento: ', camada, self.d, self.y1, CENTER)
        self.__labels.labelsInputs('Estado Cívil: ', camada, self.d, self.y2, CENTER)
        self.__labels.labelsInputs('Nacionalidade: ', camada, self.d, self.y3, CENTER)

        nasc = self.input(camada, self.d, self.a)
        eCivil = self.input(camada, self.d, self.b)
        nacionalidade = self.input(camada, self.d, self.c)

        self.__botao.criarBotao(
            camada, 'Salvar', 0.4, 0.83, 1, 5, lambda: [
                self.__tratar.salvar_dados(self.__nome, nasc, 'DataNascimento'),
                self.__tratar.salvar_dados(self.__nome, eCivil, 'EstadoCivil'),
                self.__tratar.salvar_dados(self.__nome, nacionalidade, 'Nacionalidade')
            ]
        )

    def criarInputsRedes(self, camada):
        self.__labels.labelsInputs('Facebook: ', camada, self.d, self.y1, CENTER)
        self.__labels.labelsInputs('Instagram: ', camada, self.d, self.y2, CENTER)
        self.__labels.labelsInputs('Linkedin: ', camada, self.d, self.y3, CENTER)
        face = self.input(camada, self.d, self.a)
        insta = self.input(camada, self.d, self.b)
        linkedin = self.input(camada, self.d, self.c)
        self.__botao.criarBotao(camada,'Salvar',0.4,0.83,1,5, lambda: [
                self.__tratar.salvar_dado_estrangeiro(face, self.__nome, 'Facebook', 'redes'),
                self.__tratar.salvar_dado_estrangeiro(insta, self.__nome, 'Instagram', 'redes'),
                self.__tratar.salvar_dado_estrangeiro(linkedin, self.__nome, 'Linkedin', 'redes')
            ]
        )

    def criarInputsAdicionais(self, camada, tabela):
        valores = {'x1': 0.5, 'y1': 0.12, 'y2': 0.28, 'y3': 0.44, 'y4': 0.60, 'y5': 0.76}
        a1 = self.input(camada, valores.get('x1'), valores.get('y1'))
        a2 = self.input(camada, valores.get('x1'), valores.get('y2'))
        a3 = self.input(camada, valores.get('x1'), valores.get('y3'))
        a4 = self.input(camada, valores.get('x1'), valores.get('y4'))
        a5 = self.input(camada, valores.get('x1'), valores.get('y5'))
        colunas = ['Dado1', 'Dado2', 'Dado3', 'Dado4', 'Dado5',]
        dados = [a1, a2, a3, a4, a5]
        self.__botao.criarBotao(camada,'Salvar',0.4,0.83,1,5,
                                lambda : self.__tratar.salvar_dados_lista(self.__nome, colunas, dados, tabela
        ))

    def criarInputsTexto(self, camada):
        texto = tk.Text(camada,font=("Arial", 12), height=14, width=19, bg='light gray')
        texto.place(relx=0.09, rely=0.075)

    def buildInputs(self, a, b, c, d, e, f, g, h, i):
        self.criarInputsDados(a)
        self.criarInputsContato(b)
        self.criarInputsPessoais(c)
        self.criarInputsRedes(d)
        self.criarInputsAdicionais(e,'cursos')
        self.criarInputsAdicionais(f, 'conhecimentos')
        self.criarInputsAdicionais(g, 'experiencias')
        self.criarInputsAdicionais(h, 'formacoes')
        self.criarInputsTexto(i)