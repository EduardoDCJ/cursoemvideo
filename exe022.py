# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo.
# Quantas letras tem o primeiro nome.

nome = str(input("Insira seu nome completo: ")).strip()

# O nome com todas as letras maiúsculas e minúsculas.
print(nome.upper(), '\n', nome.lower())

# Quantas letras ao todo.
qnt = len(nome) - nome.count(' ')
print(qnt)

# Quantas letras tem o primeiro nome.
primeiro_nome = nome.split()
print(len(primeiro_nome[0]))
