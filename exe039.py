# Faça um programa que leia o ano de nascimento de um jovem e informe,
# conforme a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nasc = int(input('Informe seu ano de nascimento '))
sexo = str(input('Digite [f] se for do sexo feminino e [m] se for masculino '))
atual = date.today().year
idade = atual - nasc

if idade < 18 and sexo == 'm':
    saldo = 18 - idade
    print('Você tem {} anos e ainda vai se alistar ao serviço militar daqui há {} anos'.format(idade, saldo))
elif idade > 18 and sexo == 'm':
    saldo = idade - 18
    print('Você tem {} anos e passou  há {} do tempo para se alistar'.format(idade, saldo))
elif idade == 18 and sexo == 'm':
    print('Você tem {} anos e está na idade exata para se alistar'.format(idade))
elif sexo != 'm':
    print('Você não é obrigada a se alistar')
