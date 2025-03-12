#  Escreva um programa que leia um número N inteiro qualquer
#  e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#  Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
num = int(input('Quantos elementos deseja ver \n'))
primeiro = 0
segundo = 1
cont = 0
num -= 3
print('{} - {} - '.format(primeiro, segundo), end='')
while cont <= num:
    terceiro = primeiro + segundo
    print('{} - '.format(terceiro), end='')
    primeiro = segundo
    segundo = terceiro
    cont += 1
print('FIM')
