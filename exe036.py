# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Informe o valor da casa R$ '))
salario = float(input('Informe seu salario R$ '))
anos = int(input('Informe em quantos anos irá pagar '))
parcela = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a parcela será de R${:.2f}'.format(casa, anos, parcela))
percentual = salario * 0.30

if parcela <= percentual:
    print('EMPRÉSTIMO APROVADO')
else:
    print('EMPRÉSTIMO NEGADO')
