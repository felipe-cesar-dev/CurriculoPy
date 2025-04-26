import sqlite3 as sq

class RecuperarDados():
    def __init__(self):
        pass

    def selectall(self):
        conexao = sq.connect('curriculo.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM pessoas")
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()

        return resultados