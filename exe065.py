# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
parada = None
media = quant = soma = maior = menor = 0
while parada != 'n':
    num = int(input('Digite um valor '))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    parada = str(input('Deseja parar?[S/N] ')).lower().strip()[0]
media = soma/quant
print('A soma de todos os {} números foi de {} \nA media entre eles foi de {} \nO maior deles {} \nO menor {}'
      .format(quant, soma, media, maior, menor))
