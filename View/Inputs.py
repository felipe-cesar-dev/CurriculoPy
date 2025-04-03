from tkinter.constants import CENTER

from View.ClassesAbstratas.InputsABS import InputsABC
import tkinter as tk


class Inputs(InputsABC):
    def __init__(self):
        super().__init__()
        self.__input = None

    def input(self, camada):
        input = tk.Entry(camada, bg='light gray')
        return input

    def criarInputs(self, camada):
        self.__input = self.input(camada)
        self.__input.place(relx = 0.7, rely= 0.7, anchor= CENTER)