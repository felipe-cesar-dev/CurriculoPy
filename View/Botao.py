from Controler.ClassesAbstratas.ControleBotoesABS import ControleBotoesABS
from View.ClassesAbstratas.BotaoABS import BotaoABS
import tkinter as tk

class Botao(BotaoABS):
    def __init__(self, clicar: ControleBotoesABS):
        super().__init__()
        self.__clicar = clicar

    def criarBotao(self, camada, texto, x, y, h, w, comando, armazenar, inputs, espacamento):
        def comandoa():
            comando()
            self.__clicar.botaoclicado(botao, inputs, botaoeditar)

        def comandob():
            comando()
            self.__clicar.botaoclicadoEditar(botao, inputs, botaoeditar)
        botao = tk.Button(text= texto, height=h, width=w, font=('Arial', 12), bg='green', fg='white',
                          disabledforeground='lightgray',
                          command= comandoa, state='disabled')
        botao.place(in_=camada, relx=x, rely=y)
        botaoeditar = tk.Button(text= 'Editar', height=h, width=w, font=('Arial', 12), bg='red', fg='white',
                          disabledforeground='lightgray',
                          command=comandob, state='disabled')
        botao.place(in_=camada, relx=x, rely=y)
        botaoeditar.place(in_=camada, relx=x+espacamento, rely=y)
        armazenar.append(botao)

    def criarBotaoNome(self, camada, texto, x, y, h, w, comando, armazenar):
        botao = tk.Button(text= texto, height=h, width=w, font=('Arial', 12), bg='green', fg='white',
                          command=comando, name='nomeSalvo')
        botao.place(in_=camada, relx=x, rely=y)
        armazenar.append(botao)
