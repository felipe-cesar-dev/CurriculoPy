from Model.RecuperarDados import RecuperarDados

class ControleRecuperarDados:
    def __init__(self, recuperar: RecuperarDados):
        self.__recuperar = recuperar

    def selectall(self):
        self.__recuperar.selectall()