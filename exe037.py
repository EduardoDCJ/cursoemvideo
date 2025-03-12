# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))

print('Escolha qual base de conversão ')
contador = int(input('''
 1 para binário 
 2 para octal
 3 para hexadecimal 
  '''))
match contador:
    case 1:
        print('O número {} convertido para binário será {}'.format(num, bin(num)))
    case 2:
        print('O número {} convertido para octal será {}'.format(num, oct(num)))
    case 3:
        print('O número {} convertido para hexadecimal será {}'.format(num, hex(num)))
