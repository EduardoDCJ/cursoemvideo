#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
while True:
    aleatorio = random.randint(0, 5)
    descobrir = int(input('Tente adivinhar o número entre 0 e 5 que a máquina escolheu '))
    if aleatorio == descobrir:
        print('Parabéns! Você acertou!')
    else:
        print('Que pena! Você errou! a máquina escolheu {}'.format(aleatorio))
