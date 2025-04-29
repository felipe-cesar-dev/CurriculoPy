from Controller.ClassesAbstratas.ControleBotoesABS import ControleBotoesABS


class ControleBotoes(ControleBotoesABS):
    def __init__(self):
        super().__init__()
        pass

    def botaoclicado(self, botao, inputs, botaoeditar):
        if isinstance(inputs, list):
            for entry in inputs:
                entry.config(state="disabled")
                pass
        elif isinstance(inputs, object):
            inputs.config(state="disabled")
            pass
        botao.config(state="disabled")
        botaoeditar.config(state = 'normal')

    def botaoclicadoEditar(self, botao, inputs, botaoeditar):
        if isinstance(inputs, list):
            for entry in inputs:
                entry.config(state="normal")
                pass
        elif isinstance(inputs, object):
            inputs.config(state="normal")
            pass
        botao.config(state="normal")
        botaoeditar.config(state = 'disabled')