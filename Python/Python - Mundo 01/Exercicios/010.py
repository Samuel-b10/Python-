# Exercício 10 - Crie um programa que leia quanto dinheiro 
# uma pessoa tem na carteira e mostre quantos dólares ela pode 
# comprar | considere = US$1,00 = R$5,59


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
valor = float(input('Quanto vc tem na carteira: '))

# Declarando variavel e atribuindo um calculo a ela
dolar = valor / 5.59 

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
print(f'Vc pode compra {dolar:.2f} dolares.')

# Pular linha "\n"
print("\n")
