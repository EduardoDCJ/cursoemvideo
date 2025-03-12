# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# – EQUILÁTERO: todos os lados iguais
#
# – ISÓSCELES: dois lados iguais, um diferente
#
# – ESCALENO: todos os lados diferentes
r1 = float(input('Primeiro segmento '))
r2 = float(input('Segundo segmento '))
r3 = float(input('Terceiro segmento '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos conseguem formar um triângulo ')
    if r1 == r2 and r1 == r3:
        print('Forma um triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Forma um triângulo isósceles')
    else:
        print('Forma um triângulo escaleno')
else:
    print('Os segmentos não formam um triângulo')

