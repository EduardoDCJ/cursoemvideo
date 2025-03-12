# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
nomes = []
idades = []
sexos = []
mulheres = 0
velho = None
for c in range(0, 4):
    print('----dados da {}° pessoa----'.format(c+1))
    nome = input('Informe seu nome: ').lower()
    nomes.append(nome)
    idade = int(input('Informe sua idade: '))
    idades.append(idade)
    sexo = input('Informe seu sexo[M/F]: ').lower()
    sexos.append(sexo)
    if sexo == 'f' and idade < 20:
        mulheres += 1
    if idade > 0 and sexo == 'm':
        velho = nome
media = sum(idades)/4
print('A média de idade no grupo é de {}'.format(media))
print('nome do homem mais velho: {}'.format(velho))
print('A quantidade de mulheres menores de 20 anos é {}'.format(mulheres))

