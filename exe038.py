# Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro valor é maior que o segundo')
elif n2 > n1:
    print('O segundo valor é maior que o primeiro')
else:
    print('Os valores são iguais')
