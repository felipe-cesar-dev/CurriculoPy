import tkinter as tk

class Tela:
    def __init__(self):
        self.tk = tk.Tk()
        self.tk.geometry("1280x760")
        self.tk.title("Crie seu currículo")

        self.camada1 = tk.Canvas(self.tk, bg='#0E003F')
        self.camada1.pack(fill=tk.BOTH, expand=True)

        self.camada2 = tk.Canvas(self.camada1, width=1156, height=732, bg='#283EB8', highlightthickness=0)
        self.camada2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.criarSessoes()
        self.criarLabels()

    def criarLabels(self):
        label1 = self.Labels('Dados Pessoais')
        label1.place(relx=0.124, rely=0.035, anchor=tk.CENTER)

        label2 = self.Labels('Informações de Contato')
        label2.place(relx=0.374, rely=0.035, anchor=tk.CENTER)

        label3 = self.Labels('Informações Pessoais')
        label3.place(relx=0.624, rely=0.035, anchor=tk.CENTER)

        label4 = self.Labels('Redes Sociais')
        label4.place(relx=0.874, rely=0.035, anchor=tk.CENTER)

        label5 = self.Labels('Cursos')
        label5.place(relx=0.1095, rely=0.41, anchor=tk.CENTER)

        label6 = self.Labels('Conhecimentos')
        label6.place(relx=0.305, rely=0.41, anchor=tk.CENTER)

        label7 = self.Labels('Experiências')
        label7.place(relx=0.5, rely=0.41, anchor=tk.CENTER)

        label8 = self.Labels('Formação Acadêmica')
        label8.place(relx=0.695, rely=0.41, anchor=tk.CENTER)

        label9 = self.Labels('Sobre Mim')
        label9.place(relx=0.89, rely=0.41, anchor=tk.CENTER)

    def Labels(self, texto):
        label = tk.Label(self.camada2, text=texto, bg='#283EB8', font=('Arial', 16), fg='white')
        return label

    def criarSessoes(self):
        sessao1 = self.sessao(255, 227)
        sessao1.place(relx=0.124, rely=0.22, anchor=tk.CENTER)

        sessao2 = self.sessao(255, 227)
        sessao2.place(relx=0.374, rely=0.22, anchor=tk.CENTER)

        sessao3 = self.sessao(255, 227)
        sessao3.place(relx=0.624, rely=0.22, anchor=tk.CENTER)

        sessao4 = self.sessao(255, 227)
        sessao4.place(relx=0.874, rely=0.22, anchor=tk.CENTER)

        sessao5 = self.sessao(216, 342)
        sessao5.place(relx=0.1095, rely=0.68, anchor=tk.CENTER)

        sessao6 = self.sessao(216, 342)
        sessao6.place(relx=0.305, rely=0.68, anchor=tk.CENTER)

        sessao7 = self.sessao(216, 342)
        sessao7.place(relx=0.5, rely=0.68, anchor=tk.CENTER)

        sessao8 = self.sessao(216, 342)
        sessao8.place(relx=0.695, rely=0.68, anchor=tk.CENTER)

        sessao9 = self.sessao(216, 342)
        sessao9.place(relx=0.89, rely=0.68, anchor=tk.CENTER)

    def sessao(self, w, h):
        sessao = tk.Canvas(self.camada2, width=w, height=h, bg='#ffffff', highlightthickness=0)
        return sessao

    def run(self):
        self.tk.mainloop()

if __name__ == "__main__":
    tela = Tela()
    tela.run()