# Exercício 11 - faça um programa que leia a largura e a altura 
# de uma parede em metros calcule a sua área e a quantidade de tinta 
# necessária para pintá-la sabendo que cada litro de tinta pinta uma 
# área de 2 metros cúbicos


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

#  Pede para o usuario digitar um numero de ponto flutuante para uma determinada variavel
# "input" e expecifica o tipo de variavel "float"
altura = float(input('Qual a altura da parede: '))
largura =  float(input('Qual a largura da pare: '))

# Declarando variaveis e atribuindo um calculo a elas
area = altura * largura
tinta = area / 2 

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print" | "f" e utilizado para concatenar variaveis
print(f'Vai precisar de {tinta:.2f} litros de tinta para pintar uma parede de área é {area}')

# Pular linha "\n"
print("\n")
