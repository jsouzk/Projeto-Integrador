import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Carregar as perguntas de um arquivo Excel
df = pd.read_excel('questions.xlsx')
questions = df.sample(n=15).values.tolist()

# Criando a janela
janela = tk.Tk()
janela.title('Jogo de Perguntas e Respostas')
janela.geometry("800x600")

# Cores do quiz
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
janela.config(bg=background_color)
janela.option_add('Font', 'Arial')

# Variáveis para controlar o quiz
current_question = 0
score = 0

# Função para exibir a pergunta e as opções
def show_question():
    global current_question, score

    # Limpar a janela
    for widget in janela.winfo_children():
        widget.destroy()

    # Obter a pergunta e as opções
    question = questions[current_question]
    pergunta = question[0]
    opcoes = question[1:5]
    resposta_correta = question[5]

    # Exibir a pergunta
    pergunta_label = tk.Label(janela, text=pergunta, font=("Arial", 20), bg=background_color)
    pergunta_label.pack(pady=20)

    # Função para verificar a resposta
    def verificar_resposta(opcao):
        global score, current_question

        if opcao == resposta_correta:
            score += 1

        # Próxima pergunta ou fim do quiz
        current_question += 1
        if current_question < len(questions):
            show_question()
        else:
            messagebox.showinfo("Fim do Quiz", f"Você acertou {score} de {len(questions)} perguntas!")
            janela.quit()

    # Definir as letras para as opções
    letras = ['a', 'b', 'c', 'd']

    # Exibir as opções com letras (a, b, c, d)
    for i, opcao in enumerate(opcoes):
        button = tk.Button(janela, text=f"{letras[i]}. {opcao}", font=("Arial", 16), bg=button_color, command=lambda i=i: verificar_resposta(i+1))
        button.pack(pady=10)

# Iniciar o quiz
show_question()

# Rodar a interface
janela.mainloop()
