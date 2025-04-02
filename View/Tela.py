import tkinter as tk
from View.Labels import Labels
from View.ClassesAbstratas.LabelsABS import LabelsAbstrata
from View.ClassesAbstratas.SessoesABS import SessoesAbstrata
from View.Sessoes import Sessoes

class Tela:
    def __init__(self, sessao: SessoesAbstrata, label: LabelsAbstrata):
        self.tk = tk.Tk()
        self.tk.geometry("1280x760")
        self.tk.title("Crie seu currículo")
        self.camada1 = tk.Canvas(self.tk, bg='#0E003F')
        self.camada1.pack(fill=tk.BOTH, expand=True)
        self.camada2 = tk.Canvas(self.camada1, width=1156, height=732, bg='#283EB8', highlightthickness=0)
        self.camada2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.sessoes = sessao
        self.labels = label
        sessoes.criarSessoes(self.camada2)
        label.criarLabels(self.camada2)


    def run(self):
        self.tk.mainloop()

labels = Labels()
sessoes = Sessoes()
tela = Tela(sessoes, labels)
tela.run()