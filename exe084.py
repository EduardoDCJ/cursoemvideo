# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
# Minha resolução
pessoa = []
lista = list()
resp = 's'
while resp == 's':
    n = str(input('Informe seu nome: ')).upper().strip()
    pessoa.append(n)
    p = float(input('Informe seu peso: '))
    pessoa.append(p)
    resp = input('Deseja continuar?[s/n]').lower()[0]
lista = pessoa[:]
print(f'{len(lista)/2} pessoas foram cadastradas')
pesado = pessoa[1::2]
metade = int(len(pesado)/2)
pesado.sort(reverse=True)
print(f'maiores pesos {pesado[:metade]}')
leve = pessoa[1::2]
metade = int(len(leve)/2)
leve.sort()
print(f'menores pesos {leve[:metade]}')
#curso em video
pessoa = []
lista = list()
resp = 's'
pesado = leve = 0
while resp == 's':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesado = leve = pessoa[1]
    else:
        if pessoa[1] > pesado:
            pesado = pessoa[1]
        if pessoa[1] < leve:
            leve = pessoa[1]
    lista.append(pessoa[:])
    pessoa.clear()
    resp = input('Deseja continuar?[s/n]').lower()[0]
qnt_pessoa = int(len(lista))
print(f'Houve {qnt_pessoa} pessoas cadastradas')
print(f'o maior peso foi de {pesado}. ', end='')
for p in lista:
    if p[1] == pesado:
        print(p[0])
print()
print(f'o menor peso foi de {leve}. ', end='')
for p in lista:
    if p[1] == leve:
        print(p[0])
