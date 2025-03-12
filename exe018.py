# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input("Insira o angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"o angulo de {angulo} tem seno de {seno:.2f}")
print(f"o angulo de {angulo} tem cosseno de {cosseno:.2f}")
print(f"o angulo de {angulo} tem tangente de {tangente:.2f}")

