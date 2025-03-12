# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = None
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Informe o sexo[M/F] ')).lower()
    print('Você informou o sexo {}'.format(sexo))
print('Obrigado')
