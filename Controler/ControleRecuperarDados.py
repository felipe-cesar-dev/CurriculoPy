from Model.RecuperarDados import RecuperarDados

class ControleRecuperarDados:
    def __init__(self, recuperar: RecuperarDados):
        self.__recuperar = recuperar

    def selectall(self):
        resultados = self.__recuperar.selectall()
        dados = []
        for linha_tupla in resultados:
            array_da_linha = list(linha_tupla)  # Converte a tupla em uma lista
            dados.append(array_da_linha)

        return dados