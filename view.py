import sqlite3 as lite


#criação funções CRUD
#CREATE, READY, UPDATE, DELETE

#criando conexão com o banco
con = lite.connect('bancoforms.db')


#Inserir informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)

#Acessar informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista


#Atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia=?, estado=?, assunto=? where id=?"
        cur.execute(query,i)


#Deletar informações
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query,i)
    

