#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

cidade = str(input('Digite o nome da cidade: ').upper())

maxi = cidade.split()
if maxi[0] == 'SANTO':
    print('O nome da cidade começa com "Santo"')

else:
    print('O nome da cidade não começa com "Santo"')
