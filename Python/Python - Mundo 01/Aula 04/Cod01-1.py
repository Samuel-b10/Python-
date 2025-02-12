# Aula 04 - Utilizando Módulos - Importação de bibliotecas

# Importar blibliotecas com "import ...".

import math # Biblioteca = Matematica 

# Importar somente uma parte da blibliotecas com "from ... import ...".

from math import sqrt, ceil, floor

num = int(input('digite um numero: '))

# Raiz quadrada normal = "math.sqrt(...)".

raiz = math.sqrt(num)

print("\n")

print(f'A raiz quagrada de {num} é {raiz}')

print("\n")

# Raiz quadrada arredondada pra cima = "math.ceil(...)".

print(f'A raiz quagrada de {num} é {math.ceil(raiz)}')

print("\n")

# Raiz quadrada arredondada pra baixo = "math.floor(...)".

print(f'A raiz quagrada de {num} é {math.floor(raiz)}')

print("\n")



