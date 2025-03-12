# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:

cadastro = list()
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).lower()[0]
        if pessoa['sexo'] in 'mf':
            break
        print('DIGITE UM VALOR VÁLIDO[M/F]')
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa['nome'])
    cadastro.append(pessoa['sexo'])
    cadastro.append(pessoa['idade'])
    while True:
        r = str(input('Deseja continuar?[s/n] ')).lower()[0]
        if r in 'sn':
            break
        print('DIGITE UM VALOR VÁLIDO[S/N]')
    if r == 'n':
        break
print('-='*30)
# A) Quantas pessoas foram cadastradas
print(f'A quantidade de pessoas cadastradas foi {len(cadastro)/3}')
# B) A média de idade
print('-='*30)
media = 0
for c in range(2, len(cadastro), 3):
    media += cadastro[c]
media = media/(len(cadastro)/3)
print(f'A média de idade foi {media:.2f}')
print('-='*30)
# C) Uma lista com as mulheres
print('As mulheres cadastradas foram', end=' ')
for c in range(len(cadastro)):
    if cadastro[c] == 'f':
        print(cadastro[c-1], end=' ')
print()
print('-='*30)
# D) Uma lista de pessoas com idade acima da média
print('As pessoas com idade acima da média são ')
for c in range(2, len(cadastro), 3):
    if cadastro[c] > media:
        print(cadastro[c-2], end=' ')
