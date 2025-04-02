import tkinter as tk

from View.ClassesAbstratas.LabelsABS import LabelsAbstrata


class Labels(LabelsAbstrata):
    def __init__(self):
        super().__init__()
        self.__labelDados = None
        self.__labelInfosC = None
        self.__labelInfosP = None
        self.__labelRedes = None
        self.__labelCursos = None
        self.__labelConhec = None
        self.__labelExp = None
        self.__labelForm = None
        self.__labelSobre = None

    def criarLabels(self, camada):
        self.__labelDados = self.labels('Dados Pessoais', camada)
        self.__labelDados.place(relx=0.124, rely=0.035, anchor=tk.CENTER)

        self.__labelInfosC = self.labels('Informações de Contato', camada)
        self.__labelInfosC.place(relx=0.374, rely=0.035, anchor=tk.CENTER)

        self.__labelInfosP = self.labels('Informações Pessoais', camada)
        self.__labelInfosP.place(relx=0.624, rely=0.035, anchor=tk.CENTER)

        self.__labelRedes = self.labels('Redes Sociais', camada)
        self.__labelRedes.place(relx=0.874, rely=0.035, anchor=tk.CENTER)

        self.__labelCursos = self.labels('Cursos', camada)
        self.__labelCursos.place(relx=0.1095, rely=0.41, anchor=tk.CENTER)

        self.__labelConhec = self.labels('Conhecimentos', camada)
        self.__labelConhec.place(relx=0.305, rely=0.41, anchor=tk.CENTER)

        self.__labelExp = self.labels('Experiências', camada)
        self.__labelExp.place(relx=0.5, rely=0.41, anchor=tk.CENTER)

        self.__labelForm = self.labels('Formação Acadêmica', camada)
        self.__labelForm.place(relx=0.695, rely=0.41, anchor=tk.CENTER)

        self.__labelSobre = self.labels('Sobre Mim', camada)
        self.__labelSobre.place(relx=0.89, rely=0.41, anchor=tk.CENTER)

    def labels(self, texto, camada):
        label = tk.Label(camada, text=texto, bg='#283EB8', font=('Times', 14), fg='white')
        return label




