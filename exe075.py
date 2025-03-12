# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.
num = (
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
    int(input('Digite um valor: ')),
)
print(f'o número 9 apareceu {num.count(9)} vezes')
print(f'o número 3 apareceu na {num.index(3)+1}ª posição')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
