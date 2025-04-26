from Model.RecuperarDados import RecuperarDados

class ControleRecuperarDados:
    def __init__(self, recuperar: RecuperarDados):
        self.__recuperar = recuperar

    def selectall(self, tabela):
        resultados = self.__recuperar.selectall(tabela)
        dados = []
        for linha_tupla in resultados:
            array_da_linha = list(linha_tupla)  # Converte a tupla em uma lista
            dados.append(array_da_linha)
        return dados

    def criar_li(self, dados):
        if len(dados) > 0:
            lista_html = "".join(f"<li>{valor}</li>" for valor in dados[0][1:] if valor)
            if lista_html:
                return f"<ul>{lista_html}</ul>"
            else:
                return ""
