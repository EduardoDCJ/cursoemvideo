# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from tabulate import tabulate
jogador = dict()
gerenciamento = list()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    qnt_partida = int(input('Quantas partidas jogadas? '))
    gols.clear()
    for c in range(qnt_partida):
        gols.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['tot_gols'] = sum(gols)
    gerenciamento.append(jogador.copy())
    while True:
        resp = str(input('deseja continuar?[s/n] ')).lower()[0]
        if resp in 'sn':
            break
    if resp == 'n':
        break
for j in gerenciamento:
    print(f'O jogador {j["nome"]} teve um total de {j["tot_gols"]} gols e jogou {len(j["gols"])} partidas')

# Após conhecer a biblioteca tabulate, achei adequado utilizá-la nesse código para uma melhor visualização dos dados
print(tabulate(gerenciamento, headers='keys', showindex=True, tablefmt='fancy_grid'))
