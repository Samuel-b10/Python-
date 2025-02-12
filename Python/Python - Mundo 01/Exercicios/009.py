# Exercício 09 - Faça um programa que leia um número 
# inteiro qualquer e mostre na tela a sua tabuada


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Declarando variavel e atribuindo valor
cont = 1

# Pede para o usuario digitar um numero para uma determinada variavel
# "input" e expecifica o tipo de variavel "int"
num1 = float(input('Digite um número: '))

# Pular linha "\n"
print("\n")

# Estilizando a tabuada
print('=' * 18)

# Loop para gerar a tabuada "while" | "cont <= 10" = enquanto o contador for menor ou igual a 10
while cont <= 10:

    # Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
    print(f'{num1} x {cont:2} = {num1 * cont:2.0f}')
    cont += 1

# Estilizando a tabuada
print('=' * 18)

# Pular linha "\n"
print("\n")
