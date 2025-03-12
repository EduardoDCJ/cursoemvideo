# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo')
print(type(n))
print(n.isalnum(), n.isalpha(), n.islower(), n.isspace())
