import tkinter as tk

from View.ClassesAbstratas.SessoesABS import SessoesAbstrata
from View.Sessoes import Sessoes

class Tela:
    def __init__(self, sessao: SessoesAbstrata):
        self.tk = tk.Tk()
        self.tk.geometry("1280x760")
        self.tk.title("Crie seu currículo")
        self.camada1 = tk.Canvas(self.tk, bg='#0E003F')
        self.camada1.pack(fill=tk.BOTH, expand=True)
        self.camada2 = tk.Canvas(self.camada1, width=1156, height=732, bg='#283EB8', highlightthickness=0)
        self.camada2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.criarLabels()
        self.sessoes = sessao
        sessoes.criarSessoes(self.camada2)

    def criarLabels(self):
        label1 = self.Labels('Dados Pessoais', self.camada2)
        label1.place(relx=0.124, rely=0.035, anchor=tk.CENTER)

        label2 = self.Labels('Informações de Contato', self.camada2)
        label2.place(relx=0.374, rely=0.035, anchor=tk.CENTER)

        label3 = self.Labels('Informações Pessoais', self.camada2)
        label3.place(relx=0.624, rely=0.035, anchor=tk.CENTER)

        label4 = self.Labels('Redes Sociais', self.camada2)
        label4.place(relx=0.874, rely=0.035, anchor=tk.CENTER)

        label5 = self.Labels('Cursos', self.camada2)
        label5.place(relx=0.1095, rely=0.41, anchor=tk.CENTER)

        label6 = self.Labels('Conhecimentos', self.camada2)
        label6.place(relx=0.305, rely=0.41, anchor=tk.CENTER)

        label7 = self.Labels('Experiências', self.camada2)
        label7.place(relx=0.5, rely=0.41, anchor=tk.CENTER)

        label8 = self.Labels('Formação Acadêmica', self.camada2)
        label8.place(relx=0.695, rely=0.41, anchor=tk.CENTER)

        label9 = self.Labels('Sobre Mim', self.camada2)
        label9.place(relx=0.89, rely=0.41, anchor=tk.CENTER)

    def Labels(self, texto, camada):
        label = tk.Label(camada, text=texto, bg='#283EB8', font=('Times', 14), fg='white')
        return label





    def run(self):
        self.tk.mainloop()

sessoes = Sessoes()
tela = Tela(sessoes)
tela.run()