# Exercício 19 - um professor que é sortear um dos seus quatro 
# alunos para pagar o quadro faça um programa que ajude ele lendo 
# o nome deles e escrevendo o nome do escolhido


# Importando a biblioteca "import ...".
import os 
import random

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar o nome de um aluno para uma determinada variavel
# "input" e expecifica o tipo de variavel "str" 
prim = str(input('Primeiro aluno: '))
seg = str(input('Segundo aluno: ')) 
ter = str(input('Terceiro aluno: '))
qua = str(input('Quarto aluno: '))

# Criando uma lista com os alunos utilizando um vetor "[]".
list = [prim, seg, ter, qua]

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
# "random.choice([prim, seg, ter, qua])" = escolhe um aluno aleatoriamente
print(f'O aluno escolhido foi: {random.choice(list)}')

# Pular linha "\n"
print("\n")
