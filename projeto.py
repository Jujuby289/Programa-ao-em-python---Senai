
import sqlite3 # banco de dados
import tkinter as tk # interface 
from tkinter import messagebox # caixas de mensagens
from tkinter import ttk # interface grafica tb
import customtkinter
def conectar():
    return sqlite3.connect('teste.db')


def criar_tabela():
    conn = conectar()
    c= conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        livro TEXT NOT NULL,
        data INTEGER NOT NULL,
        email TEXT NOT NULL              
        )       
    ''')
    conn.commit()
    conn.close()
  


# CREATE
def inserir_usuario():
    nome = entry_nome.get()
    livro = entry_livro.get()
    data = entry_data.get()
    email = entry_email.get()
    numero =  entry_numero.get()
    if nome and livro and data and email:
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(id,nome,livro,data,email) VALUES(?,?,?,?,?)', (numero, nome, livro, data, email))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS COM SUCESSO!') 
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRADO!') 

# READ
def mostrar_usuario():
    for row in tree.get_children():   
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()    
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for usuario in usuarios:
        tree.insert("", "end", values=(usuario[0], usuario[1],usuario[2],usuario[3],usuario[4]))
    conn.close()    


# DELETE
def delete_usuario():
    dado_del = tree.selection()
    if dado_del:
       user_id = tree.item(dado_del)['values'][0]
       conn = conectar()
       c = conn.cursor()    
       c.execute('DELETE FROM usuarios WHERE id = ? ',(user_id,))
       conn.commit()
       conn.close()
       messagebox.showinfo('', 'DADO DELETADO')
       mostrar_usuario()

    else:
       messagebox.showerror('', 'OCORREU UM ERRO')  

# UPDATE 
       
def editar():
     selecao = tree.selection()
     if selecao:
         user_id = tree.item(selecao)['values'][0]
         novo_nome = entry_nome.get()
         novo_email = entry_email.get()

         if novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()    
            c.execute('UPDATE usuarios SET nome = ? , email = ? WHERE id = ? ',(novo_nome,novo_email,user_id))
            conn.commit()
            conn.close()  
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()

         else:
             messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

     else:
            messagebox.showerror('','ALGO DEU ERRADO!')


janela = tk.Tk()
janela.title('CRUD')

label_nome = customtkinter.CTkLabel(janela, text='Nome:')
label_nome.grid(row=0, column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)


label_livro = tk.Label(janela, text='livro:')
label_livro.grid(row=1, column=0, padx=10, pady=10)

entry_livro = tk.Entry(janela)
entry_livro.grid(row=1, column=1, padx=10, pady=10)


label_data = tk.Label(janela, text='data de retirada:')
label_data.grid(row=2, column=0, padx=10, pady=10)

entry_data = tk.Entry(janela)
entry_data.grid(row=2, column=1, padx=10, pady=10)


label_email = tk.Label(janela, text = 'E-mail:')
label_email.grid(row=3, column=0, padx=10, pady=10)

entry_email = tk.Entry(janela, text = 'E-mail:')
entry_email.grid(row=3, column=1, padx=10, pady=10)



label_numero = tk.Label(janela, text = 'Numero:')
label_numero.grid(row=4, column=0, padx=10, pady=10)

entry_numero = tk.Entry(janela, text = 'Numero:')
entry_numero.grid(row=4, column=1, padx=10, pady=10)



btn_salvar = customtkinter.CTkButton(janela, text='Salvar', command=inserir_usuario)
btn_salvar.grid(row=5, column=0, padx=10, pady=10)

btn_deletar = customtkinter.CTkButton(janela, text='deletar', command=delete_usuario )
btn_deletar.grid(row=6, column=0, padx=10, pady=10)

btn_atualizar = customtkinter.CTkButton(janela, text='atualizar', command=editar)
btn_atualizar.grid(row=7, column=0, padx=10, pady=10)



columns = ('ID', 'NOME','LIVRO','DATA RETIRADA', 'E-MAIL')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=8,column=0,columnspan=2,padx=10, pady=10)


for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()


janela.mainloop()
