# Exercício 20 - O mesmo professor do desafio anterior quer sortear  ordem de 
# apresentação de trabalho dos alunos. Faça um progama que leia o nome dos 
# quadro alunos e mostre a ormdem sorteada


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

# "random.shuffle(list)" = embaralha a lista
random.shuffle(list)

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
print(f'A ordem de apresentação será: {list}')

# Pular linha "\n"
print("\n")
