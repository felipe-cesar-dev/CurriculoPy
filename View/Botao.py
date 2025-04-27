from Controler.ClassesAbstratas.ControleBotoesABS import ControleBotoesABS
from View.ClassesAbstratas.BotaoABS import BotaoABS
import tkinter as tk
from View.CurriculoHTML import CurriculoHTML

class Botao(BotaoABS):
    def __init__(self, clicar: ControleBotoesABS, gerarHTML: CurriculoHTML):
        super().__init__()
        self.__clicar = clicar
        self.__gerarHTML = gerarHTML
        self.__cor = '#159202'

    def criarBotao(self, camada, texto, x, y, h, w, comando, armazenar, inputs, espacamento):
        def comandoa():
            comando()
            self.__clicar.botaoclicado(botao, inputs, botaoeditar)

        def comandob():
            self.__clicar.botaoclicadoEditar(botao, inputs, botaoeditar)

        botao = tk.Button(text= texto, height=h, width=w, font=('Arial', 12), bg=self.__cor, fg='white',
                          disabledforeground='lightgray',
                          command= comandoa, state='disabled')
        botao.place(in_=camada, relx=x, rely=y)
        botaoeditar = tk.Button(text= 'Editar', height=h, width=w, font=('Arial', 12), bg='#ff4242', fg='white',
                          disabledforeground='lightgray',
                          command=comandob, state='disabled')
        botao.place(in_=camada, relx=x, rely=y)
        botaoeditar.place(in_=camada, relx=x+espacamento, rely=y)
        armazenar.append(botao)

    def criarBotaoNome(self, camada, texto, x, y, h, w, comando, armazenar):
        botao = tk.Button(text= texto, height=h, width=w, font=('Arial', 12), bg=self.__cor, fg='white',
                          command=comando, name='nomeSalvo', disabledforeground='lightgray')
        botao.place(in_=camada, relx=x, rely=y)
        armazenar.append(botao)
        self.criarBotaoHTML(camada, armazenar)

    def criarBotaoHTML(self, camada, armazenar):
        botao = tk.Button(text= 'Gerar Currículo', height=1, width=13, font=('Arial', 12), bg=self.__cor, fg='white',
                          command=lambda : self.__gerarHTML.criar_e_abrir_pagina(), name='html',
                          disabledforeground='lightgray', state='disabled')
        botao.place(in_=camada, relx=2.2, rely=2.95, anchor='s')
        armazenar.append(botao)
