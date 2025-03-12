# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição[{linha}][{coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*30)
# A) A soma de todos os valores pares digitados.
print(f'A soma de todos os valores pares digitados na matriz é: {pares}')
print('-='*30)
# B) A soma dos valores da terceira coluna.
terceira_col = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna: {terceira_col}')
print('-='*30)
# C) O maior valor da segunda linha.
maior = 0
if matriz[1][0] > maior:
    maior = matriz[1][0]
    if matriz[1][1] > maior:
        maior = matriz[1][1]
        if matriz[1][2] > maior:
            maior = matriz[1][2]
print(f'O maior valor da segunda linha foi: {maior}')
print('-='*30)
