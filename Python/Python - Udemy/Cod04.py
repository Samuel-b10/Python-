# Código em python: processamento de dados e casting


# Calculo de area de um trapezio

# declarando variaveis: todas float
b1: float; b2: float; h: float; area: float

# atribuindo valores
b1 = 6.0
b2 = 8.0
h = 5.0

# calculo 
area = (b1 + b2) / 2.0 * h

# saida do resultado
print(area) 

# Calculo de divisão: com somente inteiros so que o resultado vai ser float
a: int; b: int; resultado: int

a = 5
b = 2

resultado = a / b

print(resultado)
# O resultado vai ser 2.5, mesmo atribuido o valor int no resultado
# Pois o python reconhece a "/" como uma divisão com ponto flutuante
# Para sair um numero inteiro deve-se usar "//" (divisão inteira)

# Mesmo caso do anterior
x: float
z: int

x = 5.2
z = x

print(z)
# O resultado vai ser 5.2, mesmo atribuido o valor int no "z"
