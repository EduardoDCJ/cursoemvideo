# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor
# e o maior valor que estão na tupla.
import random

aleatorio = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
             , random.randint(0, 10), random.randint(0, 10))
print(f'Foi sorteado os seguintes números: {aleatorio}'
      f'\nonde o maior deles foi {max(aleatorio)}'
      f'\ne o menor foi {min(aleatorio)}')
