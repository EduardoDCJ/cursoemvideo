# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
frase = str(input('Escreva uma frase: ')).strip().upper()
frase = frase.split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase {} é um palindromo'.format(junto))
else:
    print('A frase {} não é um palindromo'.format(junto))
