import tkinter as tk

def mostrar():
    texto =  nome,idade,email.get()
    botao.config(text = texto)


janela  = tk.Tk()

janela.geometry('300x300')


tk.Label(janela, text= 'FOMULARIO').pack()

nome = tk.Label(janela, text=' Digite seu nome').pack()
nome  = tk.Entry(janela)
nome.pack()

idade = tk.Label(janela, text='Digite sua idade').pack()
idade  = tk.Entry(janela)
idade.pack()


email = tk.Label(janela, text=' Digite seu email email').pack()
email  = tk.Entry(janela)
email.pack()


tk.Button(janela, text='Mostrar',font=('arial', 15), command=mostrar).pack(pady=30)

botao = tk.Label(janela, text = '', font=('arial', 15))
botao.pack(pady=12)

janela.mainloop()