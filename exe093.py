# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
gerenciamento = dict()
gols = list()
gerenciamento['jogador'] = str(input('Nome do jogador: '))
qnt_partida = int(input('Quantas partidas jogadas? '))
for c in range(qnt_partida):
    gols.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
gerenciamento['gols'] = gols[:]
gerenciamento['tot_gols'] = sum(gols)
#
print(gerenciamento)
#
print(f'o jogador {gerenciamento["jogador"]} jogou {len(gerenciamento["gols"])} partidas')
for i, v in enumerate(gerenciamento['gols']):
    print(f'=> na {i+1}ª partida fez {v} gols')
print(f'Total de {gerenciamento["tot_gols"]} gols')
