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

    def criarSessoes(self):
        sessao1 = self.sessao()
        sessao1.place(relx=0.124, rely=0.22, anchor=tk.CENTER)

        sessao2 = self.sessao()
        sessao2.place(relx=0.374, rely=0.22, anchor=tk.CENTER)

        sessao3 = self.sessao()
        sessao3.place(relx=0.624, rely=0.22, anchor=tk.CENTER)

        sessao4 = self.sessao()
        sessao4.place(relx=0.874, rely=0.22, anchor=tk.CENTER)

    def sessao(self):
        sessao = tk.Canvas(self.camada2, width=255, height=227, bg='#ffffff', highlightthickness=0)
        return sessao

    def run(self):
        self.tk.mainloop()

if __name__ == "__main__":
    tela = Tela()
    tela.run()