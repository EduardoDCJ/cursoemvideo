# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [1] somar
#
# [2] multiplicar
#
# [3] maior
#
# [4] novos números
#
# [5] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.
escolha = 6
while escolha != 5:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    escolha = int(input(' [1] SOMAR \n [2] MULTIPLICAR \n '
                        '[3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA \n'))
    if escolha == 1:
        res = n1 + n2
        print('A soma entre {} e {} = {}'.format(n1, n2, res))
    elif escolha == 2:
        res = n1 * n2
        print('A multiplicação entre {} e {} = {}'.format(n1, n2, res))
    elif escolha == 3:
        if n1 > n2:
            print('O {} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('O {} é maior que {}'.format(n2, n1))
        else:
            print('Os números são iguais')
    elif escolha == 4:
        print('Escolha novos números')
print('Obrigado')
