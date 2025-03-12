# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
pessoas = []
for c in range(0, 5):
    peso = float(input('Informe seu peso: '))
    pessoas.append(peso)
pesado = max(pessoas)
leve = min(pessoas)
print(' O maior peso lido foi de {}Kg \n O menor peso foi de {}Kg'.format(pesado, leve))
