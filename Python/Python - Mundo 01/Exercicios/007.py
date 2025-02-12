# Exercício 04 - Desenvolva um programa que leia as 
# duas notas de um aluno calcule e mostre a sua média


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
num1 = float(input('Digite uma nota: '))
num2 = float(input('Digite outra nota: '))

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
# "{(num1 + num2) / 2:.2f}" = calcula a media entre as notas | {...:.2f} = exibe apenas 2 casas decimais
print(f'A media entra as notas de {num1:.1f} e {num2:.1f} são: {(num1 + num2) / 2:.2f}')

# Pular linha "\n"
print("\n")
