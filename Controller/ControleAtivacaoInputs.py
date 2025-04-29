from Controller.ClassesAbstratas.ControleAtivacaoInputsABS import ControleAtivacaoInputsABS
import tkinter as tk


class ControleAtivacaoInputs(ControleAtivacaoInputsABS):
    def __init__(self):
        super().__init__()
        pass

    def ativar_tudo(self, ativar, entradas, textos):
        ativar = 'normal'
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

    def ativar_botoes(self, botoes, ativar, nome):
        ativar = 'normal'
        self.atualizar_botoes(botoes, ativar, nome)
        return ativar

    def atualizar_botoes(self, botoes, ativar, nome):
        for botao in botoes:
            try:
                botao.config(state=ativar)
            except tk.TclError:
                pass

        nome.config(state = 'disabled')

