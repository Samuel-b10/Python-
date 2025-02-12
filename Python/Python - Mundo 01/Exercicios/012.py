# Exercício 12 - Faça um algoritmo que leia o preço de um produto e 
# mostre seu novo preço com 5% de desconto


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
valor = float(input('Digite o preço de um produto: '))

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
# "{valor - (valor * 5/100)}" = calcula o desconto do produto
print(f'O produto com 5% de desconto fica: {valor - (valor * 5/100):.2f}')

# Pular linha "\n"
print("\n")
