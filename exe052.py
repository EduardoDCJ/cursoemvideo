#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número inteiro '))
lista = 0
for c in range(1, num + 1):
    if num % c == 0:
        lista += 1
if lista == 2:
    print('o {} é um número primo'.format(num))
else:
    print('o {} não é um número primo'.format(num))
