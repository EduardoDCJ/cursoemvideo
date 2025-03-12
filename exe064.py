# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando a flag).
num = int(input('Tente acertar o valor de parada '))
limite = 999
total = 0
contador = 0
while num != limite:
    total += num
    contador += 1
    num = int(input('Tente outro valor '))
print('A soma de todos os {} valores tentados {}'.format(contador, total))
