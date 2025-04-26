import sqlite3 as sq

class RecuperarDados():
    def __init__(self):
        pass

    def selectall(self):
        conexao = sq.connect('curriculo.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM pessoas")
        resultados = cursor.fetchall()
        dados = []  # Inicializa uma lista para conter os "arrays" (listas)

        for linha_tupla in resultados:
            array_da_linha = list(linha_tupla)  # Converte a tupla em uma lista
            dados.append(array_da_linha)

        cursor.close()
        conexao.close()