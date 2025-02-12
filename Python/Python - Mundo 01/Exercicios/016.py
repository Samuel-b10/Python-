# Exercício 16 - crie um programa que leia um número real 
# qualquer pelo teclado e mostre na tela a sua posição inteira


# Importando a biblioteca "import ...".
import os 
import math

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
num = float(input('Digite um numero real: '))

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
print(f'O numero {num} tem a parte inteira de: {num:.0f}')

# OU
 
# Pular linha "\n"
print("\n")

# math.trunc(...) = retorna a parte inteira de um numero
print(f'O numero {num} tem a parte inteira de: {math.trunc(num)}')  

# Pular linha "\n"
print("\n")
