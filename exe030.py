# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Escreva um número para saber se é impar ou par: '))

if numero % 2 == 0:
    print('O número {} é par'.format(numero))
else:
    print('O número {} é impar'.format(numero))
