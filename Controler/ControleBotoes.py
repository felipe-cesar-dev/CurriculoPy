from Controler.ClassesAbstratas.ControleBotoesABS import ControleBotoesABS


class ControleBotoes(ControleBotoesABS):
    def __init__(self):
        super().__init__()
        pass

    def botaoclicado(self, botao, inputs):
        if isinstance(inputs, list):
            for entry in inputs:
                entry.config(state="disabled")
                pass
        elif isinstance(inputs, object):
            inputs.config(state="disabled")
            pass
        botao.config(state="disabled")