# Exercício 18 - faça um programa que leia um ângulo qualquer 
# e mostre na tela o valor do seno cosseno e tangente desse ângulo


# Importando a biblioteca "import ...".
import os 
import math

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
ângulo = float(input('Digite um angulo: '))

sen = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tan = math.tan(math.radians(ângulo))

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
print(f'Com o angulo de {ângulo} o Seno vale: {sen:.2f}')
print(f'Com o angulo de {ângulo} o Cosseno vale: {cos:.2f}')
print(f'Com o angulo de {ângulo} a Tangente vale: {tan:.2f}')

# Pular linha "\n"
print("\n")
