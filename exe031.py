# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200Km
# e R$ 0,45 para viagens mais longas.

distancia = float(input('Informe a distancia em Km '))
if distancia <= 200:
    passagem = distancia * 0.50
    print('Percorrendo {} km, o preço da passagem será de {}'.format(distancia, passagem))
else:
    passagem = distancia * 0.45
    print('Percorrendo {} km, o preço da passagem será de {}'.format(distancia, passagem))
