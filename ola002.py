import tkinter as tk
from tkinter import messagebox

# Cria uma janela
root = tk.Tk()
root.withdraw()  # Esconde a janela principal

# Exibe a caixa de mensagem
messagebox.showinfo("Mensagem", "Olá Usuário!")

# Mantém a janela aberta
root.mainloop()