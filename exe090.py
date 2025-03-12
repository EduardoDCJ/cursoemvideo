# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
fichario = list()
dados = dict()

dados['nome'] = str(input('Nome aluno: '))
dados['media'] = float(input(f'Media de {dados['nome']}: '))
if dados['media'] >= 7:
    dados['situaçao'] = 'aprovado'
else:
    dados['situaçao'] = 'reprovado'
fichario.append(dados.copy())
for c in fichario:
    for k, v in dados.items():
        print(f'{k} é {v}')
