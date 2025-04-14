import sqlite3 as sq

from Model.TratarDadosABS import TratarDadosABS


class TratarDados(TratarDadosABS):
    def __init__(self):
        super().__init__()
        pass

    def salvar_nome(self, nome):
        conn = sq.connect('curriculo.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pessoas (Nome) VALUES (?)", (nome,))
        conn.commit()
        conn.close()

    def salvar_dado(self, nome, dado, coluna):
        conn = sq.connect('curriculo.db')
        cursor = conn.cursor()
        cursor.execute(f"UPDATE pessoas SET {coluna} = ? WHERE Nome = ?", (dado, nome))
        conn.commit()
        conn.close()

    def salvar_dado_estrangeiro(self, dado, nome, coluna):
        conn = sq.connect('curriculo.db')
        cursor = conn.cursor()
        cursor.execute(f"UPDATE redes SET {coluna} = ? WHERE pessoa_nome = ?", (dado, nome))
        if cursor.rowcount == 0:
            cursor.execute(f"INSERT INTO redes (pessoa_nome, {coluna}) VALUES (?, ?)", (nome, dado))
        conn.commit()
        conn.close()

    def limparTodosDados(self):
        conn = sq.connect('curriculo.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pessoas;")
        cursor.execute("DELETE FROM redes")
        conn.commit()
        conn.close()