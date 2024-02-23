import sqlite3 as lite

# criando conexão
con = lite.connect('bancoforms.db')

# criando tabela
with con:
    cursor = con.cursor()
    cursor.execute(
        "CREATE table formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia Date, estado TEXT, assunto TEXT)")
