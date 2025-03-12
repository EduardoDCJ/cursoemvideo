# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
ca = float(input("Insira o valor do cateto adjacente: "))
co = float(input("Insira o valor do cateto oposto: "))
h = (co**2 + ca**2) ** (1/2)
hi = hypot(ca, co)
print(hi)
print(h)
