# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Qual número deseja ver a tabuada? '))
    if num < 0:
        break
    for cont in range(0, 11):
        print(f'{num}x{cont}={num*cont}')
