# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
numeros = []
soma = 0
for c in range(6):
    numero = int(input('Digite o {}° número '.format(c+1)))
    numeros.append(numero)
    if numero % 2 == 0:
        soma += numero
print(soma)
