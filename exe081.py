# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
resp = 's'
num_5 = 0
while resp == 's':
    numero = int(input('digite um valor: '))
    lista.append(numero)
    resp = input('Deseja continuar?[s/n]')
print(f'A quantidade de números digitados foi {len(lista)}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente {lista}')
for i in range(len(lista)):
    if 5 == lista[i]:
        num_5 += 1
if num_5 > 0:
    print(f'O número 5 apareceu {num_5} vezes')
else:
    print('O número 5 não apareceu nessa lista')
