# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

times = ('ATLÉTICO-MG', 'BAHIA', 'BOTAFOGO', 'CEARÁ SC', 'CORINTHIANS', 'CRUZEIRO', 'FLAMENGO', 'FLUMINENSE',
         'FORTALEZA', 'GRÊMIO', 'INTERNACIONAL', 'JUVENTUDE', 'MIRASSOL', 'PALMEIRAS', 'BRAGANTINO', 'SANTOS',
         'SPORT RECIFE', 'SÃO PAULO', 'VASCO DA GAMA', 'EC VITÓRIA')

# a) Os 5 primeiros times.
for c in range(5):
    print(f'O {c+1}° colocado é {times[c]}')

# b) Os últimos 4 colocados.
print(f'os 4 últimos times são {times[-4:]}')

# c) Times em ordem alfabética.
print(f'os times em ordem alfabética {sorted(times)}')

# d) Em que posição está o time da Flamengo.
print(f'O flamengo está na {times.index("FLAMENGO")+1}° posição')
