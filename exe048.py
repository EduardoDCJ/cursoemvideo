# Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Os números múltiplos de 3 são')
soma = 0
cont = 0
for c in range(1, 501):
    multiplo = c % 3
    if multiplo == 0:
        cont += 1
        soma += + c
print(cont, soma)
