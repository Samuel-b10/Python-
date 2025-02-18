# Aula 05 - Manipulando Texto - Fatiamento e Análise de Strings


# Importando a biblioteca "import ...".
import os 

# "os.system('cls')" = limpa o terminal | 
os.system('cls')


# Declarando variaveis e atribuindo valor 
frase = 'Curso em Video Python'


print('=' * 30)
print("\n")


# Fatiamento de Strings 


# Extraindo somente uma parte da frase, no caso o [3] = "s"
print(frase[3])
print("\n")

# Extraindo do [3] ao [12] pois elimina o [13]
print(frase[3:13])
print("\n")

# Extraindo do inicio ao [12] pois elimina o [13]
print(frase[:13])
print("\n")

# Extraindo do [15] ao final
print(frase[15:])
print("\n")

# Extraindo do [1] ao [14] pulando de 2 em 2
print(frase[1:15:2])
print("\n")

# Extraindo do [1] ao final pulando de 2 em 2
print(frase[1::2])
print("\n")

print('=' * 30)
print("\n")

# Análise de Strings

# Quantidade de letras da frase
print(len(frase))
print("\n")

# Conta quantas vezes o "o" aparece na frase
print(frase.count('o'))
print("\n")

# Conta quantas vezes o "o" aparece na frase, do [0] ao [12], pois o [13] nao conta
print(frase.count('o', 0, 13))
print("\n")

# Conta aonde o "deo" aparece na frase, e mostra quando começou o "deo" no caso [11]
print(frase.find('deo'))
print("\n")

# Conta aonde o "Android" aparece na frase, e mostra quando começou o "Android" no caso [-1]
# Se nao encontrar ele retorna -1
print(frase.find('Android'))
print("\n")


print('=' * 30)
print("\n")


# Transformação de Strings


# Encontra o "Python" e substituir por "Android"
# "replace" = substitui
print(frase.replace('Python', 'Android'))
print("\n")

# Transformando todas as letras em maiusculas
print(frase.upper())
print("\n")

# Transformando todas as letras em minusculas
print(frase.lower())
print("\n")

# Transformando todas as letras em minusculas e somente a  primeira letra em maiuscula
print(frase.capitalize())
print("\n")

# Transforma a primerira letra de cada palavra em maiuscula
print(frase.title())
print("\n")

frase2 = '   Aprenda Python  '

# Retira os espaços inutils em branco da frase
print(frase2.strip())
print("\n")

# Retira os espaços inutils em branco da frase somente na direita
print(frase2.rstrip())
print("\n")

# Retira os espaços inutils em branco da frase somente na esquerda
print(frase2.lstrip())
print("\n")


print('=' * 30)
print("\n")


# Divisão de Strings



print("\n")
