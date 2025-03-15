#  Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
#  início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

def contador(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print(i)


# a) de 1 até 10, de 1 em 1
print('de 1 até 10, de 1 em 1')
contador(1, 11, 1)

# b) de 10 até 0, de 2 em 2
print('de 10 até 0, de 2 em 2')
contador(10, -1, -2)

# c) uma contagem personalizada
começo = int(input('Começo: '))
final = int(input('Final: '))
progressão = int(input('Progressão: '))
contador(começo, final, progressão)
