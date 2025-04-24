import sqlite3 as sq
from Model.TratarDadosABS import TratarDadosABS

class TratarDados(TratarDadosABS):
    def __init__(self):
        super().__init__()
        pass

    def salvar_nome(self, nome):
        try:
            conn = sq.connect('curriculo.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pessoas (Nome) VALUES (?)", (nome,))
            conn.commit()
            conn.close()
        except sq.Error as e:
            print(f"Erro ao salvar dado: {e}")

    def salvar_dado(self, nome, dado, coluna):
        try:
            conn = sq.connect('curriculo.db')
            cursor = conn.cursor()
            cursor.execute(f"UPDATE pessoas SET {coluna} = ? WHERE Nome = ?", (dado, nome))
            conn.commit()
            conn.close()
        except sq.Error as e:
            print(f"Erro ao salvar dado: {e}")

    def salvar_dado_estrangeiro(self, dado, nome, coluna, tabela):
        try:
            conn = sq.connect('curriculo.db')
            cursor = conn.cursor()
            cursor.execute(f"UPDATE {tabela} SET {coluna} = ? WHERE pessoa_nome = ?", (dado, nome))
            if cursor.rowcount == 0:
                cursor.execute(f"INSERT INTO {tabela} (pessoa_nome, {coluna}) VALUES (?, ?)", (nome, dado))
            conn.commit()
            conn.close()
        except sq.Error as e:
            print(f"Erro ao salvar dado: {e}")

    def salvar_dados_lista(self, nome, coluna, dados, tabela):
        try:
            nomeCapturado = nome[0]
            conn = sq.connect('curriculo.db')
            cursor = conn.cursor()
            for i in range(len(coluna)):
                cursor.execute(f"UPDATE {tabela} SET {coluna[i]} = ? WHERE pessoa_nome = ?",
                               (dados[i].get().title(), nomeCapturado))
                if cursor.rowcount == 0:
                    cursor.execute(f"INSERT INTO {tabela} (pessoa_nome, {coluna[i]}) VALUES (?, ?)",
                                   (nomeCapturado, dados[i].get().title()))
            conn.commit()
            conn.close()
        except sq.Error as e:
            print(f"Erro ao salvar dado: {e}")

    def limparTodosDados(self):
        conn = sq.connect('curriculo.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pessoas;")
        cursor.execute("DELETE FROM redes")
        cursor.execute("DELETE FROM conhecimentos")
        cursor.execute("DELETE FROM cursos")
        cursor.execute("DELETE FROM formacoes")
        cursor.execute("DELETE FROM sobremim")
        cursor.execute("DELETE FROM experiencias")
        conn.commit()
        conn.close()