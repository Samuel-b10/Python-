# Código em python: Entrada de dados 

print("\n")

# Declarando variaveis
salario1: float; salario2: float
nome1: str; nome2: str
idade: int
sexo: str

# Entrada de dados

nome1 = input("Digite o primeiro nome: ")
salario1 = float(input("Digite o primeiro salario: "))

nome2 = input("Digite o segundo nome: ")
salario2 = float(input("Digite o segundo salario: "))

idade = int(input("Digite a idade: "))
sexo = input("Digite o sexo (M/F): ")

# pular uma linha
print("\n")

# Saida de dados com interpolção

print(f"Nome 1 = {nome1}")
print(f"Salario 1 = {salario1}")
print(f"Nome 2 = {nome2}")
print(f"Salario 2 = {salario2}")
print(f"Idade = {idade}")
print(f"Sexo = {sexo}")