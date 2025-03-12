#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Insira seu nome: ').strip().lower())

if 'silva' in nome:
    print(f' Seu nome {nome} \n tem Silva')
else:
    print(f' Seu nome {nome} \n não tem Silva')
