# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário R$ '))
if salario > 1250:
    aumento = salario * 0.10
    print('Com base no seu salario {}, o seu aumento será de {:.2f}'.format(salario, aumento))
else:
    aumento = salario * 0.15
    print('Com base no seu salario {}, o seu aumento será de {:.2f}'.format(salario, aumento))
