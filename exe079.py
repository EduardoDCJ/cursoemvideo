# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = []
resp = 's'
while resp == 's':
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
    resp = input('Deseja adicionar mais um número?[s/n] ')
numeros.sort()
print(f'A lista em ordem crescente ficou {numeros}')
