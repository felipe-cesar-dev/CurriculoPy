from Controler.ClassesAbstratas.ControleBotoesABS import ControleBotoesABS


class ControleBotoes(ControleBotoesABS):
    def __init__(self):
        super().__init__()
        pass

    def botaoclicado(self, botao, inputs):
        botao.config(state = 'disabled')
        inputs.config(state = 'disabled')