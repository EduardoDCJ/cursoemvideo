# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, conforme a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida
peso = float(input('Informe seu peso em Kg '))
altura = float(input('Informe sua altura em metros '))
potencia = pow(altura, 2)
imc = peso/potencia

if imc < 18.5:
    print('Seu IMC é de {:.1f} e você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é de {:.1f} e você está no peso normal'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é de {:.1f} e você está acima do peso'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é de {:.1f} e você está em estado de obesidade'.format(imc))
elif imc > 40:
    print('Seu IMC é de {:.1f} e você está em estado de obesidade mórbida'.format(imc))
