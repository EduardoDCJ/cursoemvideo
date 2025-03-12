import random
from time import sleep
jokenpo = ['pedra', 'papel', 'tesoura']
escolha = random.choice(jokenpo)

jogador = str(input('''Vamos Jogar JOPENKO
Escreva pedra papel ou tesoura
 para tentar ganhar de mim 8D '''))
jogador = jogador.lower().strip()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if escolha == jogador:
    print('Empatamos :) escolhemos {}'.format(escolha))
elif (escolha == 'pedra' and jogador == 'papel' or escolha == 'papel' and
      jogador == 'tesoura' or escolha == 'tesoura' and jogador == 'pedra'):
    print('Você ganhou!!! eu escolhi {} e você {}'.format(escolha, jogador))
elif (jogador == 'pedra' and escolha == 'papel' or jogador == 'papel' and
      escolha == 'tesoura' or jogador == 'tesoura' and escolha == 'pedra'):
    print('Que pena :( você perdeu!!! eu escolhi {} e você {}'.format(escolha, jogador))
