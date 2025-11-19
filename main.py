import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

# ------------------ CARREGAR PERGUNTAS ------------------
df = pd.read_excel("questions.xlsx")
questions = df.values.tolist()  # Todas as perguntas

# ------------------ VARIÁVEIS GLOBAIS ------------------
current_question = 0
score = 0
timer_value = 20
timer_id = None
botoes = []
usuario_nome = ""
janela = None
container = None
timer_label = None
progress = None
titulo_label = None

# ------------------ FUNÇÕES ------------------

def salvar_resultado(nome, pontuacao):
    """Salva o desempenho do usuário em resultados.csv"""
    resultado = pd.DataFrame([[nome, pontuacao, len(questions)]], columns=["Nome", "Acertos", "Total"])
    if os.path.exists("resultados.csv"):
        resultado.to_csv("resultados.csv", mode='a', index=False, header=False)
    else:
        resultado.to_csv("resultados.csv", index=False)

def atualizar_timer():
    global timer_value, timer_id
    timer_value -= 1
    timer_label.config(text=f"Tempo: {timer_value}")
    if timer_value == 0:
        mostrar_resultado(None)
        return
    timer_id = janela.after(1000, atualizar_timer)

def mostrar_resultado(opcao_escolhida):
    global score, timer_id
    if timer_id:
        janela.after_cancel(timer_id)
        timer_id = None

    question = questions[current_question]
    resposta_correta = question[5]

    for btn in botoes:
        idx = botoes.index(btn) + 1
        if idx == resposta_correta:
            btn.config(bg="#4CAF50", fg="white")
        elif idx == opcao_escolhida:
            btn.config(bg="#D32F2F", fg="white")

    if opcao_escolhida == resposta_correta:
        score += 1

    janela.after(1000, proxima_pergunta)

def proxima_pergunta():
    global current_question
    current_question += 1
    if current_question < len(questions):
        show_question()
    else:
        mostrar_tela_final()

def show_question():
    global timer_value, timer_id, botoes

    if timer_id:
        janela.after_cancel(timer_id)
        timer_id = None

    progress["value"] = current_question
    timer_value = 20
    timer_label.config(text=f"Tempo: {timer_value}")

    for widget in container.winfo_children():
        widget.destroy()

    question = questions[current_question]
    pergunta = question[0]
    opcoes = question[1:5]

    pergunta_label = tk.Label(
        container,
        text=pergunta,
        font=("Arial", 22, "bold"),
        wraplength=750,
        justify="center",
        bg="#F5F7FA",
        fg="#222222"
    )
    pergunta_label.pack(pady=25)

    botoes = []
    letras = ["a", "b", "c", "d"]
    for i, opcao in enumerate(opcoes):
        btn = tk.Button(
            container,
            text=f"{letras[i]}. {opcao}",
            font=("Arial", 18),
            bg="#E0E0E0",
            fg="black",
            activebackground="#BDBDBD",
            relief="raised",
            height=2,
            command=lambda i=i: mostrar_resultado(i + 1)
        )
        btn.pack(pady=10, fill="x", padx=50)
        botoes.append(btn)

    timer_id = janela.after(1000, atualizar_timer)

# ------------------ TELA INICIAL ------------------

def iniciar_quiz():
    global usuario_nome, current_question, score
    nome = nome_entry.get().strip()
    if not nome:
        messagebox.showwarning("Aviso", "Digite seu nome para iniciar o quiz.")
        return
    usuario_nome = nome
    current_question = 0
    score = 0
    tela_inicio.pack_forget()
    criar_quiz_ui()

def mostrar_participantes():
    if not os.path.exists("resultados.csv"):
        messagebox.showinfo("Participantes", "Nenhum participante registrado ainda.")
        return
    df_resultados = pd.read_csv("resultados.csv")
    info = "\n".join([f"{row['Nome']}: {row['Acertos']}/{row['Total']}" for _, row in df_resultados.iterrows()])
    messagebox.showinfo("Participantes", info)

# ------------------ TELA FINAL ------------------

def mostrar_tela_final():
    salvar_resultado(usuario_nome, score)
    for widget in container.winfo_children():
        widget.destroy()
    if timer_label:
        timer_label.destroy()
    if progress:
        progress.destroy()
    global titulo_label
    if titulo_label:
        titulo_label.destroy()

    percentual = round((score / len(questions)) * 100, 2)
    final_msg = f"{usuario_nome}, você acertou {score} de {len(questions)} perguntas!\nPercentual: {percentual}%"

    lbl_final = tk.Label(
        container,
        text=final_msg,
        font=("Arial Black", 24),
        bg="#F5F7FA",
        fg="#333333",
        justify="center"
    )
    lbl_final.pack(pady=50)

    btn_reiniciar = tk.Button(
        container,
        text="Reiniciar Quiz",
        font=("Arial", 18),
        bg="#4CAF50",
        fg="white",
        command=reiniciar_quiz
    )
    btn_reiniciar.pack(pady=20)

def reiniciar_quiz():
    global current_question, score, timer_label, progress, titulo_label
    current_question = 0
    score = 0
    if timer_label:
        timer_label.destroy()
    if progress:
        progress.destroy()
    if titulo_label:
        titulo_label.destroy()
    container.destroy()
    criar_tela_inicio()

# ------------------ UI DO QUIZ ------------------

def criar_quiz_ui():
    global container, progress, timer_label, titulo_label

    container = tk.Frame(janela, bg="#F5F7FA")
    container.place(relx=0.5, rely=0.55, anchor="center")

    progress = ttk.Progressbar(janela, length=600, mode="determinate")
    progress.place(relx=0.5, rely=0.08, anchor="center")
    progress["maximum"] = len(questions)

    titulo_label = tk.Label(
        janela,
        text="Quiz de Perguntas e Respostas",
        font=("Arial Black", 28),
        fg="#333333",
        bg="#F5F7FA"
    )
    titulo_label.place(relx=0.5, rely=0.15, anchor="center")

    timer_label = tk.Label(
        janela,
        text=f"Tempo: {timer_value}",
        font=("Arial", 20, "bold"),
        fg="#D32F2F",
        bg="#F5F7FA"
    )
    timer_label.place(relx=0.5, rely=0.25, anchor="center")

    show_question()

# ------------------ TELA INICIAL ------------------

def criar_tela_inicio():
    global tela_inicio, nome_entry
    tela_inicio = tk.Frame(janela, bg="#F5F7FA")
    tela_inicio.pack(fill="both", expand=True)

    titulo_inicio = tk.Label(
        tela_inicio,
        text="Bem-vindo ao Quiz!",
        font=("Arial Black", 32),
        fg="#333333",
        bg="#F5F7FA"
    )
    titulo_inicio.pack(pady=50)

    nome_label = tk.Label(tela_inicio, text="Digite seu nome:", font=("Arial", 20), bg="#F5F7FA")
    nome_label.pack(pady=10)

    nome_entry = tk.Entry(tela_inicio, font=("Arial", 18), width=30)
    nome_entry.pack(pady=10)

    start_btn = tk.Button(tela_inicio, text="Iniciar Quiz", font=("Arial", 18), bg="#4CAF50", fg="white", command=iniciar_quiz)
    start_btn.pack(pady=10)

    participantes_btn = tk.Button(tela_inicio, text="Ver Participantes", font=("Arial", 18), bg="#2196F3", fg="white", command=mostrar_participantes)
    participantes_btn.pack(pady=10)

# ------------------ JANELA PRINCIPAL ------------------

janela = tk.Tk()
janela.title("Quiz de Perguntas e Respostas")
janela.geometry("900x650")
janela.configure(bg="#F5F7FA")

criar_tela_inicio()
janela.mainloop()

