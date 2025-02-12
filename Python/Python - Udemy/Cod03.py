# Código em Python: Saida de dados


# Saida de dados simples com print, que ja vem com a quebra de linha na saida
print("Bom dia")
print("Boa Tarde")


# print("\n") = quebra de linha
print("\n")


# Saida de dados com print, que nao vem com a quebra de linha na saida
# utilizando o comando end=" " ou end='' , para falar que ao final não deve haver uma quebra de linha
print("Bom dia", end=" ")
print("Boa Tarde")

print("\n")

# Placeholder de formatação
# %d = int
# %f = float
# %s = string

# Formas de saida de dados com print

x = 10
y = 20
print(x); print(y)


z: float = 2.3456
print("{:.2f}".format(z))


idade: int = 32
salario: float = 4560.9
nome: str = "Maria Silva"
sexo: str = "F"

# Primeira forma de printar variaveis: interpolação de variaveis (Mais simples e legivel, mais utilizada)
print(f"A funcionaria {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")

# Segunda forma de printar variaveis (Mais complexa e complexa, menos utilizada)
print("A funcionaria {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos".format(nome, sexo, salario, idade))


print("\n")