# Exercício 08 - Escreva um programa que leia um valor 
# em metros e exiba convertido em centímetros e milímetros


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
num1 = float(input('Digite um valor em Metros: '))

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
# "{num1 * 100:.1f}" = comverte de metros para centimetros
print(f'{num1:.0f} metros e equivale a {num1 * 100:.1f} centímetros', end = ' ')

# "end = " " = para nao quebrar a linha

# "{num1 * 1000:.1f}" = comverte de metros para milimetros
print(f'e {num1 * 1000:.1f} em milímetros')

# Pular linha "\n"
print("\n")
