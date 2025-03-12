# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
import emoji
for c in range(10, 0, -1):
    print('{}'.format(c))
    time.sleep(1)
print('Os fogos de artifícios estouraram ')
print(emoji.emojize(':fireworks: :fireworks: :fireworks: :fireworks:'))
print(emoji.emojize(':sparkles: :sparkles: :sparkles: :sparkles:'))
