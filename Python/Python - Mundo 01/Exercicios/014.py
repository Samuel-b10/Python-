# Exercício 14 - Escreva um programa que converta uma temperatura digitada 
# em graus celsius e converta para Fahrenheit


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
c = float(input('Digite uma temperatura em °C = '))

# Declarando variaveis e atribuindo um calculo a elas
# "((9 * c) / 5) + 32" = converte de Celsius para Fahrenheit
f = ((9 * c) / 5) + 32

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
print(f'{c:.2f}°C equivale a {f:.2f} em Fahrenheit')

# Pular linha "\n"
print("\n")
