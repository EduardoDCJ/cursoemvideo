# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

# meu jeito
num = list()
for c in range(5):
    num.append(int(input('Digite um valor ')))
if num[0] > num[1] and num[0] > num[2] and num[0] > num[3] and num[0] > num[4]:
    print(f'O maior número é {num[0]} na posição 0')
if num[1] > num[0] and num[1] > num[2] and num[1] > num[3] and num[1] > num[4]:
    print(f'O maior número é {num[1]} na posição 1')
if num[2] > num[1] and num[2] > num[0] and num[2] > num[3] and num[2] > num[4]:
    print(f'O maior número é {num[2]} na posição 2')
if num[3] > num[0] and num[3] > num[1] and num[3] > num[2] and num[3] > num[4]:
    print(f'O maior número é {num[3]} na posição 3')
if num[4] > num[1] and num[4] > num[2] and num[4] > num[3] and num[4] > num[0]:
    print(f'O maior número é {num[4]} na posição 4')
#
if num[0] < num[1] and num[0] < num[2] and num[0] < num[3] and num[0] < num[4]:
    print(f'O menor número é {num[0]} na posição 0')
if num[1] < num[0] and num[1] < num[2] and num[1] < num[3] and num[1] < num[4]:
    print(f'O menor número é {num[1]} na posição 1')
if num[2] < num[1] and num[2] < num[0] and num[2] < num[3] and num[2] < num[4]:
    print(f'O menor número é {num[2]} na posição 2')
if num[3] < num[0] and num[3] < num[1] and num[3] < num[2] and num[3] < num[4]:
    print(f'O menor número é {num[3]} na posição 3')
if num[4] < num[1] and num[4] < num[2] and num[4] < num[3] and num[4] < num[0]:
    print(f'O menor número é {num[4]} na posição 4')
# curso em video
from operator import index
maior = menor = 0
numeros = list()
for c in range(0, 5):
    numeros.append(int(input('Digite um valor ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print(f'O maior valor foi {maior} na posição ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end='')
print('\n')
print(f'O menor valor foi {menor} na posição ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')
