# Exercício 05 -Faça um programa que leia um número 
# inteiro e mostre na tela o seu sucessor e o seu antecessor


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero para uma determinada variavel
# "input" e expecifica o tipo de variavel "int"
num = int(input('Digite um numero : '))

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
# " {num + 1} " = calcula o sucessor
print(f'O sucessor de {num} é : {num + 1}')

# Pular linha "\n"
print("\n")

# " {num - 1} " = calcula o antecessor
print(f'O antecessor de {num} é : {num - 1}')

# Pular linha "\n"
print("\n")
