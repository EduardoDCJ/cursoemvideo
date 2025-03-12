# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
numero = int(input('Digite o número para listar a tabuada '))
for c in range(0, 11):
    print('{} x {} = {}'.format(numero, c, numero * c))
