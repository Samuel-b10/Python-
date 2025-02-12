# Exercício 17 - faça um programa que leia o comprimento do cateto 
# oposto e do cateto adjacente de um triângulo retângulo, calcule e 
# mostre o comprimento da hipotenusa


# Importando a biblioteca "import ...".
import os 
import math

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

# Declarando variaveis e atribuindo um calculo a elas
# "math.hypot(co, ca)" = calcula a hipotenusa
hi = math.hypot(co, ca)

# Ou = "hi = (co**2 + ca**2)**(1/2)" | ou "hi = sqrt(co*co + ca*ca)"

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
print(f'Com o cateto oposto de {co} e o cateto adjacente de {ca} a hipotenusa vale: {hi:.2f}')


# Pular linha "\n"
print("\n")
