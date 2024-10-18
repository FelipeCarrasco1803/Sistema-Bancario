import tkinter as tk
from tkinter import messagebox

# Inicializa o saldo e a lista de transações
saldo = 0
transacoes = []

# Funções para as operações bancárias
def deposito():
    global saldo
    try:
        valor = float(entry_deposito.get())
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        saldo += valor
        transacoes.append(f"Depósito: R$ {valor:.2f}")
        atualizar_extrato()
        messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        entry_deposito.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

def saque():
    global saldo
    try:
        valor = float(entry_saque.get())
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > saldo:
            raise ValueError("Saldo insuficiente.")
        saldo -= valor
        transacoes.append(f"Saque: R$ {valor:.2f}")
        atualizar_extrato()
        messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado com sucesso!")
        entry_saque.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

def atualizar_extrato():
    listbox_transacoes.delete(0, tk.END)
    for transacao in transacoes:
        listbox_transacoes.insert(tk.END, transacao)
    label_saldo.config(text=f"Saldo Atual: R$ {saldo:.2f}")

# Tela principal (interface gráfica)
root = tk.Tk()
root.title("Sistema Bancário")

# Layout
frame = tk.Frame(root)
frame.pack(pady=20)

label_saldo = tk.Label(frame, text=f"Saldo Atual: R$ {saldo:.2f}", font=("Arial", 14))
label_saldo.grid(row=0, column=0, columnspan=2, pady=10)

# Depósito
label_deposito = tk.Label(frame, text="Valor do Depósito: R$", font=("Arial", 12))
label_deposito.grid(row=1, column=0, padx=10, pady=5)
entry_deposito = tk.Entry(frame, font=("Arial", 12))
entry_deposito.grid(row=1, column=1, padx=10, pady=5)
button_deposito = tk.Button(frame, text="Depositar", command=deposito, font=("Arial", 12))
button_deposito.grid(row=1, column=2, padx=10, pady=5)

# Saque
label_saque = tk.Label(frame, text="Valor do Saque: R$", font=("Arial", 12))
label_saque.grid(row=2, column=0, padx=10, pady=5)
entry_saque = tk.Entry(frame, font=("Arial", 12))
entry_saque.grid(row=2, column=1, padx=10, pady=5)
button_saque = tk.Button(frame, text="Sacar", command=saque, font=("Arial", 12))
button_saque.grid(row=2, column=2, padx=10, pady=5)

# Extrato
frame_extrato = tk.Frame(root)
frame_extrato.pack(pady=20)

listbox_transacoes = tk.Listbox(frame_extrato, width=50, height=10, font=("Arial", 12))
listbox_transacoes.pack()

# Inicia a interface gráfica
root.mainloop()
