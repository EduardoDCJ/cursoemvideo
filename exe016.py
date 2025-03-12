# Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input("Digite um número Real qualquer: "))
inteiro = trunc(num)

print("O número {} tem a porção inteira de {}".format(num, inteiro))
print("O número {} tem a porção inteira de {}".format(num, int(num)))
