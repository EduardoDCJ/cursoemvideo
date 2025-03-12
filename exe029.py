# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Informe sua velocidade! '))
if velocidade > 80:
    print('VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE !!! TAXADO, OTÁRIO :3')
    multa = (velocidade - 80) * 7
    print('SUA MULTA É DE R${:.2f}'.format(multa))
elif velocidade <= 80:
    print('Você passou dentro do limite de velocidade')
