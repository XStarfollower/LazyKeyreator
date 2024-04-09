import random
import string
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def criaSenha():
    
    x=random.randint(9,11)
    
    caracteres_especiais = string.punctuation

    senha = ""
    
    senha += random.choice(string.ascii_uppercase)
    
    senha += random.choice(caracteres_especiais)+random.choice(caracteres_especiais)
    
    senha += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(x))
    
    senhaFinal = "".join(random.sample(senha,len(senha)))
    
    return senhaFinal

def salvarSenha():
    
    nomeSenha = entry_Site_App.get()
    diretorio = filedialog.askdirectory()
    
    if not nomeSenha or not diretorio:
        messagebox.showerror("Erro","Por favor, preencha os campos.")
        return
    
    senhaGerada = criaSenha()
    salvarSenhaArquivo(nomeSenha, senhaGerada, diretorio)
    messagebox.showinfo("Senha Salva",f"A senha foi salva com sucesso em:\n {os.path.join(diretorio, nomeSenha)}.txt")

def salvarSenhaArquivo(nomeSenha,printSenha,diretorio):
    
    nomeFile = os.path.join(diretorio, nomeSenha + datetime.now().strftime("_%Y-%m-%d_%H-%M-%S") + ".txt")
    with open(nomeFile, 'a') as file:
        dataHora = datetime.now().strftime(" %Y-%m-%d %H:%M:%S")
        file.write(f"{printSenha} --- Senha gerada em {dataHora}: {nomeSenha}\n")
        messagebox.showinfo("Senha Gerada",f"Senha gerada em {dataHora}:{nomeSenha}\n")  

#interface 

root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("500x300")

label_Site_App = tk.Label(root, text ="Nome do aplicativo para qual a senha sera criada: ")
label_Site_App.pack()
entry_Site_App = tk.Entry(root)
entry_Site_App.pack()


botaoGerar = tk.Button(root, text = "Criar e Salvar senha", command = salvarSenha)
botaoGerar.pack()

root.mainloop()
        
    
