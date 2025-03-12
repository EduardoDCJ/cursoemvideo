# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
jogo = []
palpites = []
qnt_jogos = int(input('Quantos jogos deseja formar? '))
for j in range(qnt_jogos):
    for c in range(6):
        num = randint(1, 60)
        if num not in palpites:
            palpites.append(num)
    palpites.sort()
    jogo.append(palpites[:])
    palpites.clear()

for j in range(len(jogo)):
    print(f'jogo Nº{j+1}{jogo[j]}\n')
