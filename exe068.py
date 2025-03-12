#  Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador perder,
#  mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
print('='*40)
print('Vamos jogar par ou impar com o computador')
print('='*40)
vitoria = 0
soma = 0
while True:
    jogador = int(input('Escolha um número '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolha par ou impar[P/I] ')).upper()[0]
    computador = random.randint(1, 10)
    soma = jogador + computador
    if soma % 2 == 0 and escolha == 'P':
        print(f'{soma} Você venceu!')
        vitoria += 1
    elif soma % 2 != 0 and escolha == 'P':
        print(f'{soma} Você perdeu :(')
        break
    if soma % 2 != 0 and escolha == 'I':
        print(f'{soma} Você venceu!')
        vitoria += 1
    elif soma % 2 == 0 and escolha == 'I':
        print(f'{soma} Você perdeu :(')
        break
print(f'Você venceu {vitoria} vezes !!!')
