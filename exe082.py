# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = list()
par = list()
impar = list()
resp = 's'

while resp == 's':
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    resp = input('Deseja continuar?[s/n] ')
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print(f'lista completa={lista}')
print(f'par={par}')
print(f'impar={impar}')
