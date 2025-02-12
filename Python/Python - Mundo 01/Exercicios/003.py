# Exercício 03 - Crie um progama que leia dois números e mostre 
# a soma entre eles


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pular linha "\n"
print("\n")

# Pede para o usuario digitar um numero ou um valor para uma determinada variavel 
# "input" e expecifica o tipo de variavel "int"
num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))

# Exibe a mensagem na tela "print"
# "f" e utilizado para concatenar variaveis
print(f'O valor da some entre {num1} e {num2} é: {num1 + num2}')

# Pular linha "\n"
print("\n")
