# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Escreva seu nome completo ').strip())
divisao_nome = nome.split()
print('Seu primeiro nome é {}'.format(divisao_nome[0]))
print('Seu ultimo nome é {}'.format(divisao_nome[len(divisao_nome)-1]))
