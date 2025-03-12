# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.
maior_idade = 0
homem = 0
mulher_menos_20 = 0
while True:
    idade = int(input('Informe a idade '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Informe o sexo[F/M] ')).lower()
    if idade >= 18:
        maior_idade += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f' and idade < 20:
        mulher_menos_20 += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja informar mais dados?[S/N] ')).lower()
    if continuar == 'n':
        break
print(f'{maior_idade} pessoas são maiores de idade \n{homem} dessas pessoas são homens\n'
      f'{mulher_menos_20} dessas pessoas são mulheres menores de 20 anos')
