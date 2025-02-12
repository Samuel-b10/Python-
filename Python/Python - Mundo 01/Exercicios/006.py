# Exercício 04 - Crie um algoritmo que leia um número 
# e mostre o seu dobro triplo e raiz quadrada


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero para uma determinada variavel
# "input" e expecifica o tipo de variavel "int"
num = int(input('Digite um número: '))

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
# "{num * 2}" = calcula o dobro | "{num * 3}" = calcula o triplo
print(f'O dobro de {num} é : {num * 2}, o triplo e {num * 3}', end = " ")

# "end = " " = para nao quebrar a linha

# "{num ** (1/2)}" = calcula a raiz quadrada
print(f'e a raiz quadrada e de : {num ** (1/2)}')

# Pular linha "\n"
print("\n")
