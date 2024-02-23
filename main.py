#importando o tkinter
from tkinter import *
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from tkinter import messagebox
#importando view
from view import *

#cores utilizadas
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

#criando janela
janela = Tk()
janela.title("")
#tamanho
janela.geometry('1043x453')
#cor de fundo
janela.configure(background=co2)
#desabilitando aumento da altura da dela
#janela.resizable(width=FALSE, height=FALSE)


#dividindo as partes da janela#

#parte verde escura
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat') 
frame_cima.grid(row=0, column=0)

#parte do cadastro
frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat') 
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

#parte dos dados registrados
frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat') 
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


#Lable janela verde escura 
app_nome = Label(frame_cima,text='Formulário de Consultoria', anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co1, relief='flat') 
app_nome.place(x=10, y=20)


#variavel global
global tree


#FUNÇÃO INSERIR
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    dia = e_calendario.get()
    estado = e_estado.get()
    assunto = e_sobre.get()

    lista = [nome, email, telefone, dia, estado, assunto]

    if nome =='':
        messagebox.showerror('Erro','O nome não pode estar vazio')
    else: 
        inserir_info(lista)
        messagebox.showinfo('Sucesso','Os dados foram inseridos com suceso')

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_calendario.delete(0,'end')
        e_estado.delete(0,'end')
        e_sobre.delete(0,'end') 

    for widget in frame_direita.winfo_children():
        widget.destroy()
    
    mostrar()


#FUNÇÃO ATUALIZAR   
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_calendario.delete(0,'end')
        e_estado.delete(0,'end')
        e_sobre.delete(0,'end')

        e_nome.insert(0,tree_lista[1])
        e_email.insert(0,tree_lista[2])
        e_telefone.insert(0,tree_lista[3])
        e_calendario.insert(0,tree_lista[4])
        e_estado.insert(0,tree_lista[5])
        e_sobre.insert(0,tree_lista[6])


        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            dia = e_calendario.get()
            estado = e_estado.get()
            assunto = e_sobre.get()

            lista = [nome, email, telefone, dia, estado, assunto, valor_id]

            if nome =='':
                messagebox.showerror('Erro','O nome não pode estar vazio')
            else: 
                atualizar_info(lista)
                messagebox.showinfo('Sucesso','Os dados foram atualizados com suceso')

                e_nome.delete(0,'end')
                e_email.delete(0,'end')
                e_telefone.delete(0,'end')
                e_calendario.delete(0,'end')
                e_estado.delete(0,'end')
                e_sobre.delete(0,'end') 

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        #botao atualizar
        botao_confirmar = Button(frame_baixo,command=update, text='Confirmar',width=10, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge') 
        botao_confirmar.place(x=110, y=370)
            
        

    except IndexError:
        messagebox.showinfo('Erro','Selecione um dos dados na tabela')


#FUNÇÃO DELETAR
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Sucesso','Os dados foram deletados da Tabela com sucesso')

        for widget in frame_direita.winfo_children():
                widget.destroy()

        mostrar()
    
    except IndexError:
        messagebox.showinfo('Erro','Selecione um dos dados na tabela')



    
#Lable parte do cadastro - Nome
l_nome = Label(frame_baixo,text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat') 
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid') 
e_nome.place(x=15, y=40)

#Lable parte do cadastro - Email
l_email = Label(frame_baixo,text='Email *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat') 
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid') 
e_email.place(x=15, y=100)

#Lable parte do cadastro - Telefone
l_telefone = Label(frame_baixo,text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat') 
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid') 
e_telefone.place(x=15, y=160)

#Data da consulta
l_calendario = Label(frame_baixo,text='Data da Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat') 
l_calendario.place(x=15, y=190)
e_calendario = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024) 
e_calendario.place(x=15, y=220)

#Estado consulta
l_estado = Label(frame_baixo,text='Estado da Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat') 
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify='right', relief='solid') 
e_estado.place(x=160, y=220)

#Sobre
l_sobre = Label(frame_baixo,text='Informações complementares*', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat') 
l_sobre.place(x=15, y=260)
e_sobre = Entry(frame_baixo, width=45, justify='left', relief='solid') 
e_sobre.place(x=15, y=290)

#botao inserir
botao_inserir = Button(frame_baixo,command=inserir,text='Inserir',width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge') 
botao_inserir.place(x=15, y=340)

#botao atualizar
botao_atualizar = Button(frame_baixo,command=atualizar, text='Atualizar',width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge') 
botao_atualizar.place(x=110, y=340)

#botao deletar
botao_deletar = Button(frame_baixo,command=deletar, text='Deletar',width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge') 
botao_deletar.place(x=205, y=340)


def mostrar():

    global tree

    lista = mostrar_info()

    #lista para cabeçalho
    tabela_header = ['ID','Nome','Email','Telefone','Data','Estado','Sobre']

    #criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_header, show="headings")

    #scroll vertical
    scrollvert = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    #scroll horizontal
    scrollhori = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.yview)

    tree.configure(yscrollcommand=scrollvert.set, xscrollcommand=scrollhori.set)

    tree.grid(column=0, row=0, sticky='nsew')
    scrollvert.grid(column=1, row=0, sticky='ns')
    scrollhori.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0, weight=12)

    #alinhamento das informações dentro da janela direita
    hd=["nw","nw","nw","nw","nw","center","center"]

    #largura da coluna
    h=[30,170,140,120,50,100]
    n=0

    #configurações das informações dentro da janela
    for col in tabela_header:
        tree.heading(col, text=col.title(),anchor=CENTER)
        #tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)


#Chamando a função "mostrar"
mostrar()


janela.mainloop()