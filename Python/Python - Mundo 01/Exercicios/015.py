# Exercício 15 -Escreva um programa que pergunte a quantidade de km 
# percorrido por um carro alugado e a quantidade de dias pelo quais
# ele foi alugado calcule o preço a pagar sabendo que o carro custa 
# R$ 60 por dia e R$ 0,15 por km rodado


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero inteiro e de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "int" e "float"
dia = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km foram rodados: '))

# Pular linha "\n"
print("\n")

# Declarando variaveis e atribuindo um calculo a elas
preço = (dia * 60) + (km * 0.15)

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
print(f'O valor final a pagar é de : {preço:.2f}')

# Pular linha "\n"
print("\n")
