import os
import pandas as pd

# Lista de questões (15 originais + 10 primeiras + 15 novas = 40 questões)
questions = [
    # -------------------- SUAS PERGUNTAS ORIGINAIS --------------------
    ["Quem foi o responsável pela Proclamação da Independência do Brasil em 1822?", "Dom Pedro I", "Tiradentes", "Getúlio Vargas", "D. João VI", 1],
    ["Qual é a fórmula para calcular a área de um triângulo?", "A = b * h", "A = b * h / 2", "A = 2b + h", "A = (b * b) * h", 2],
    ["Qual é o maior rio do mundo em volume de água?", "Rio Amazonas", "Rio Nilo", "Rio Mississipi", "Rio Yangtsé", 1],
    ["Quem pintou a Mona Lisa?", "Van Gogh", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo", 3],
    ["Em que ano o Brasil foi descoberto?", "1500", "1492", "1600", "1700", 1],
    ["Quem foi o primeiro presidente dos Estados Unidos?", "Abraham Lincoln", "George Washington", "John F. Kennedy", "Thomas Jefferson", 2],
    ["Qual foi a principal causa da Primeira Guerra Mundial?", "Invasão da Polônia", "Assassinato do arquiduque Francisco Ferdinando", "Revolução Industrial", "Dissolução do Império Austro-Húngaro", 2],
    ["Qual é o elemento químico representado pelo símbolo 'O'?", "Ouro", "Oxigênio", "Ósmio", "Ozônio", 2],
    ["Qual é o maior planeta do sistema solar?", "Terra", "Saturno", "Júpiter", "Urano", 3],
    ["Qual país tem o maior número de ilhas no mundo?", "Suécia", "Indonésia", "Canadá", "Grécia", 1],
    ["Quem é o autor de 'Harry Potter'?", "J.R.R. Tolkien", "Suzanne Collins", "J.K. Rowling", "George R.R. Martin", 3],
    ["Qual banda lançou o álbum 'Abbey Road'?", "The Rolling Stones", "Queen", "The Beatles", "Pink Floyd", 3],
    ["Quem é conhecido como o 'Rei do Pop'?", "Elvis Presley", "Michael Jackson", "Prince", "Stevie Wonder", 2],
    ["Em que esporte Michael Jordan se destacou?", "Futebol", "Tênis", "Basquete", "Natação", 3],
    ["Qual é o maior continente em termos de área?", "África", "Ásia", "América", "Europa", 2],

    # -------------------- 10 PERGUNTAS DE LÓGICA (primeiro grupo) --------------------
    ["Em lógica de programação, qual estrutura é usada para repetir um bloco de código várias vezes?",
     "Condição", "Função", "Laço de repetição", "Variável", 3],

    ["O que significa o operador '==' em linguagens como Python, C e VisualG?",
     "Atribuição", "Comparação de igualdade", "Concatenação", "Incremento", 2],

    ["Em Python, qual é o resultado de: print(2 * 3 ** 2)?",
     "36", "18", "12", "24", 2],

    ["Qual é o tipo de dado usado para armazenar valores verdadeiros ou falsos?",
     "String", "Inteiro", "Booleano", "Caractere", 3],

    ["Em C, qual comando finaliza uma instrução?",
     "Dois pontos", "Ponto e vírgula", "Vírgula", "Aspas", 2],

    ["Em VisualG, qual estrutura é usada para tomada de decisão?",
     "Enquanto", "Para", "Repita", "Se...Então...Senão", 4],

    ["Qual é a saída do código Python: print(len('programacao'))?",
     "11", "10", "9", "12", 1],

    ["Em lógica de programação, uma variável serve para:",
     "Armazenar dados temporários", "Criar gráficos", "Apagar funções", "Organizar pastas", 1],

    ["Em C, qual destas é uma estrutura de repetição?",
     "switch", "if", "for", "typedef", 3],

    ["Em Python, qual destes operadores representa 'OU lógico'?",
     "&&", "||", "or", "&", 3],

    # -------------------- 15 NOVAS PERGUNTAS DE LÓGICA --------------------
    ["O que significa 'indentação' em Python?",
     "Uso de ponto e vírgula", "Espaços para definir blocos de código", "Fechar chaves", "Declarar variáveis", 2],

    ["Em C, qual palavra-chave é usada para declarar uma constante?",
     "const", "static", "define", "final", 1],

    ["No VisualG, qual comando exibe uma mensagem na tela?",
     "escrever()", "mostrar()", "imprima()", "escreva()", 4],

    ["O que o comando 'break' faz em estruturas de repetição?",
     "Reinicia o laço", "Finaliza o laço", "Pausa temporariamente", "Repete o bloco atual", 2],

    ["Qual destas estruturas representa um laço 'para' em Python?",
     "for i = 1 até 10", "for(i=0;i<10;i++)", "for i in range(10):", "loop 10 times", 3],

    ["Qual é o resultado de: print(10 // 3) em Python?",
     "3.3", "3", "4", "3.0", 2],

    ["Em C, qual operador é usado para acessar itens de um array?",
     "()", "[]", "{}", "<>", 2],

    ["Em VisualG, qual destas é a estrutura correta do 'enquanto'?",
     "enquanto(condição) { }", "enquanto condição faça", "while(condição)", "loop enquanto", 2],

    ["Em Python, qual é a função usada para ler entrada do usuário?",
     "scan()", "input()", "read()", "escreva()", 2],

    ["Qual o valor final da variável x no código em C: int x=5; x+=3;?",
     "2", "8", "15", "3", 2],

    ["No VisualG, qual comando inicia um algoritmo?",
     "início", "algoritmo", "inicio", "programa", 2],

    ["Em Python, qual destas estruturas representa uma condição?",
     "if x > 10:", "se (x > 10)", "if (x > 10)", "condição(x > 10)", 1],

    ["Em C, o que significa '&&'?",
     "OU lógico", "NÃO lógico", "E lógico", "Comparação", 3],

    ["Qual é a saída de: print(5 != 5) em Python?",
     "True", "False", "Erro", "5", 2],

    ["Em lógica de programação, um algoritmo deve ser:",
     "Confuso e longo", "Ambíguo", "Sequência de passos claros", "Sempre recursivo", 3]
]

# Criando DataFrame do pandas
df = pd.DataFrame(questions, columns=["Perguntas", "Opção 1", "Opção 2", "Opção 3", "Opção 4", "Resposta"])

# Verificando se o arquivo já existe
if os.path.exists("questions.xlsx"):
    print("O arquivo 'questions.xlsx' já existe!")
else:
    df.to_excel("questions.xlsx", index=False)
    print("Perguntas Inseridas com Sucesso")
