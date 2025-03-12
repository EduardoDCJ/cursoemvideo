# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
import random

computador = random.randint(0, 10)
jogador = 11
tentativas = 0
while jogador != computador:
    print('---- Tentativa n° {} ----'.format(tentativas + 1))
    jogador = int(input('Tente adivinhar que número \nescolheu entre 0 e 10: '))
    if jogador != computador:
        tentativas += 1
    if jogador < computador:
        print('mais... tente novamente')
    elif jogador > computador:
        print('menos ... tente novamente')
print('Você precisou de {} tentativas para acertar'.format(tentativas + 1))
