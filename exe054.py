# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
atual = datetime.date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    pessoa = int(input('Digite seu ano de nascimento '))
    idade = atual - pessoa
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(' {} são maiores de idade \n {} são menores de idade'.format(maior, menor))
