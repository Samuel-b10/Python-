# Exercício 04 - faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo e todas as informações 
# possíveis sobre ele


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')

# Pede para o usuario digitar algo ou um valor para uma determinada variavel
# "input" 
a = input('Digite algo: ')

# Pular linha "\n"
print("\n")

# Exibe a mensagem na tela "print"
# "print(type(...))" - type = Identificar qual classe a variável está.
print(type(a))

# {a.isspace()} = verifica se a variavel contém apenas espaços em branco
print(f'Só tem espaço? {a.isspace()}')

# {a.isnumeric()} = verifica se a variavel contém apenas numeros
print(f'É número? {a.isnumeric()}')

# {a.isalpha()} = verifica se a variavel contém apenas letras
print(f'É alfabético? {a.isalpha()}')

# {a.isalnum()} = verifica se a variavel contém apenas letras ou numeros
print(f'É alfanumérico? {a.isalnum()}')

# {a.isupper()} = verifica se a variavel contém apenas letras maiúsculas
print(f'Está em maiúsculas? {a.isupper()}')

# {a.islower()} = verifica se a variavel contém apenas letras minúsculas
print(f'Está em minúsculas? {a.islower()}')

# {a.istitle()} = verifica se a variavel contém apenas primeira letra maiúscula
print(f'Está capitalizada? {a.istitle()}')

# Pular linha "\n"
print("\n")
