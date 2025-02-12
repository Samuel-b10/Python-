# Aula 03 - Operadores Aritméticos em Python


print(5 + 3 * 2)
# Resultado = 11

print(5 ** 2)
# Resultado = 25

print(5 ** 3)
# Resultado = 125

print(19 // 2)
# Resultado = 9

print(19 / 2)
# Resultado = 9.5

print(18 % 2)
# Resultado = 0

print(122 % 3)
# Resultado = 2

# Formas de usar a " Potência "

print(4 ** 3)
# Resultado = 64

print(pow(4,3))
# Resultado = 64

# ==================================

# Raiz quadrada de qualquer número 

print(81 ** (1/2))
# Resultado = 9.0

print(25 ** (1/2))
# Resultado = 5.0

# Raiz cúbica de qualquer número

print(127 ** (1/3))
# Resultado = 5.026525695313479

# ==================================

# Formas de usar os operadores aritméticos junto de string

print('Oi' + 'Olá')
# Resultado = 'OiOlá'

print('Oi' * 5)
# Resultado = 'OiOiOiOiOi'

print('=' * 20)
# Resultado = '===================='


print("\n")
# =========================================================

# Forma de ultilizar a string no print

# Normal
nome = input('Qual e o seu nome? ')
print(f'Prazer em te conhecher {nome}!')
# Resultado = Prazer em te conhecher Barto!

# Escrevendo o "nome" em 20 caracteres
print(f'Prazer em te conhecher {nome:20}!')
# Resultado = Prazer em te conhecher Barto               !

# Alinhamento a direita em 20 espaços 
print(f'Prazer em te conhecher {nome:>20}!')
# Resultado = Prazer em te conhecher                Barto!
 
# Alinhamento a esquerda em 20 espaços 
print(f'Prazer em te conhecher {nome:<20}!')
# Resultado = Prazer em te conhecher Barto               !
 
# Alinhamento ao centro em 20 espaços
print(f'Prazer em te conhecher {nome:^20}!')
# Resultado = Prazer em te conhecher        Barto        !
 
print("\n")
# =========================================================

n1 = int(input('Digite um número: '))
n2 = int(input('outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f}', end = ' >>> ')
print(f'Divisão interia é {di} e potência {e}')


print("\n")



