import tkinter as tk
from View.Botao import Botao
from View.ClassesAbstratas.LabelsABS import LabelsAbstrata
from View.ClassesAbstratas.SessoesABS import SessoesAbstrata

class Tela:
    def __init__(self, sessao: SessoesAbstrata, label: LabelsAbstrata, botao: Botao):
        self.tk = tk.Tk()
        self.tk.geometry("1280x760")
        self.tk.title("Crie seu currículo")
        self.camada1 = tk.Canvas(self.tk, bg='#0E003F')
        self.camada1.pack(fill=tk.BOTH, expand=True)
        self.camada2 = tk.Canvas(self.camada1, width=1156, height=732, bg='#283EB8', highlightthickness=0)
        self.camada2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.sessoes = sessao
        self.botao = botao
        self.labels = label
        self.sessoes.criarSessoes(self.camada2)
        self.labels.criarLabels(self.camada2)
        self.botao.criarBotao(self.camada2,'Gerar Currículo', 0.35, 0.95, 1, 13, 'assasas')
        self.botao.criarBotao(self.camada2, 'Limpar Campos', 0.48, 0.95, 1, 13, 'asasdasdsa')

    def run(self):
        self.tk.mainloop()


