# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


def sorteia(lista):
    for i in range(5):
        lista.append(randint(0, 100))


num = []
sorteia(num)


def soma_par():
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(f'Dos valores {num} a soma dos pares foi {soma}')


soma_par()
