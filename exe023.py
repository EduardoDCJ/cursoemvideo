#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input("Insira um número entre 0 e 9999: "))

if num >= 0 and num < 10000:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print('a unidade é {}'.format(u))
    print('a dezena é {}'.format(d))
    print('a centena é {}'.format(c))
    print('a milhar é {}'.format(m))

else:
    print('O número não está entre 0 e 9999')

print(f'seu número é {num}')
