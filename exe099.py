# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(lista):
    m = 0
    for i in lista:
        if i > m:
            m = i
    print(f'Dos valores {lista}, o maior deles é {m}')


num = list()
while True:
    n = int(input('Digite um número inteiro: '))
    num.append(n)
    while True:
        r = str(input('Deseja inserir mais algum número? ')).lower()[0]
        if r in 'sn':
            break
    if r == 'n':
        break

maior(num)
