# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = []
par = []
impar = []
for c in range(7):
    lista.append(int(input('Digite um valor: ')))
for n in lista:
    if n % 2 == 0:
        par.append(n)
for n in lista:
    if n % 2 != 0:
        impar.append(n)
par.sort()
impar.sort()
print(f'números pares:{par} \nnúmeros impares:{impar}')
