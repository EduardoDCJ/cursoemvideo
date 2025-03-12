# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
ano_atual = date.today().year
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Informe o sexo[M/F]: ')).lower()[0]
cadastro['idade'] = ano_atual - nasc
cadastro['ctps'] = int(input('Possui CTPS?(digite 0 se não tiver): '))
if cadastro['ctps'] != 0:
    cadastro['salario'] = float(input('Informe o salário: R$'))
    contratacao = int(input('Ano de contratação: '))
    cadastro['contratacao'] = contratacao
    if sexo == 'm':
        cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - date.today().year)
    if sexo == 'f':
        cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 30) - date.today().year)

for k, v in cadastro.items():
    print(f'{k} tem valor {v}')
