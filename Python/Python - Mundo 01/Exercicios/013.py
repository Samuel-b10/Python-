# Exercíco 13 - faça um algoritmo que leia o salário de um funcionário 
# e mostre seu novo salário com 15% de aumento


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
sal = float(input('Digite um salario: '))

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
# "{sal + (sal * 15/100)}" = calcula o aumento do salario
print(f'O sálario com 15% de aumento: {sal + (sal * 15/100):.2f}')

# Pular linha "\n"
print("\n")
