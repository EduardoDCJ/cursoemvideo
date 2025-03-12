# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número '))
c = num
fatorial = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    fatorial = fatorial * c
    c -= 1
print('\n{}! é igual a {}'.format(num, fatorial))
