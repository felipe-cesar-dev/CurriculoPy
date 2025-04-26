import sqlite3 as sq

class RecuperarDados():
    def __init__(self):
        pass

    def selectall(self, tabela):
        conexao = sq.connect('curriculo.db')
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM {tabela}")
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()

        return resultados