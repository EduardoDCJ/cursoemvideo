# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

produto = float(input('Informe o valor do produto: '))
metodo = int(input('''[1] para pagamento à vista dinheiro/cheque 
[2] para pagamento à vista no cartão
[3] para parcelamento até 2x no cartão
[4] para parcelamento 3x ou mais no cartão
'''))

if metodo == 3 or metodo == 4:
    qnt_parcela = int(input('Informe em quantas vezes irá parcelar '))
match metodo:
    case 1:
        desconto = produto * 0.90
        print('Você teve 10% de desconto. O valor a ser pago será de {}'.format(desconto))
    case 2:
        desconto = produto * 0.95
        print('Você teve 5% de desconto. O valor a ser pago será de {}'.format(desconto))
    case 3:
        parcela = produto / qnt_parcela
        print('Você parcelou em {} e as parcelas ficaram de {}'.format(qnt_parcela, parcela))
    case 4:
        juros = produto * (20/100)
        acrescimo = produto + juros
        parcela = acrescimo / qnt_parcela
        print('Você parcelou em {} e o preço total do produto com juros é de {}. Parcelas de {}'.format(qnt_parcela, acrescimo, parcela))
