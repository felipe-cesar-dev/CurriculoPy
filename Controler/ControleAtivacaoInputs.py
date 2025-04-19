from Controler.ControleAtivacaoInputsABS import ControleAtivacaoInputsABS
import tkinter as tk


class ControleAtivacaoInputs(ControleAtivacaoInputsABS):
    def __init__(self):
        super().__init__()
        pass

    def ativar_tudo(self, ativar, entradas, textos):
        ativar = 'normal'
        print(ativar)
        self.__atualizar_estados(entradas, ativar, textos)
        return ativar

    def __atualizar_estados(self, entradas, ativar, textos):
        for entrada in entradas:
            try:
                entrada.config(state=ativar)
            except tk.TclError:
                pass  # Lidar com widgets que podem ter sido destruídos

        for texto in textos:
            try:
                texto.config(state=ativar)
            except tk.TclError:
                pass  # Lidar com widgets que podem ter sido destruídos