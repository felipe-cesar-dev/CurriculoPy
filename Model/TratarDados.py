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

    def salvar_profissao(self, nome, profissao):
        conn = sq.connect('curriculo.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE pessoas SET Profissao = ? WHERE Nome = ?", (profissao, nome))
        conn.commit()
        conn.close()

    def limparTodosDados(self):
        conn = sq.connect('curriculo.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pessoas;")
        conn.commit()
        conn.close()