# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, conforme a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER
from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de seu nascimento '))
idade = atual - nasc

if idade <= 9:
    print('Você tem {} e sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} e sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} e sua categoria é JUNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} e sua categoria é SÊNIOR'.format(idade))
elif idade > 25:
    print('Você tem {} e sua categoria é MASTER'.format(idade))
