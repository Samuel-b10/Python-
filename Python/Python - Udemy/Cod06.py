# ódigo em python: Estrutura Condicional

print("\n")

# Declarando variaveis

x = 10

print("Bom dia")

# Estrutura Condicional Simples

if x < 0:
    print("Boa Tarde")

print("Boa Noite")

print("\n")

# Declarando variaveis

hora: int
hora2: int

hora = int(input("Digite a hora: "))

# Estrutura Condicional Composta

if hora < 12:
    print("Bom Dia")
else:
    print("Boa Tarde")

print("\n")

hora2 = int(input("Digite a hora: "))

# Estrutura Condicional Encadeamento

if hora2 < 12:
    print("Bom Dia")
elif hora2 < 18:
    print("Boa Tarde")
else:
    print("Boa Noite")

print("\n")