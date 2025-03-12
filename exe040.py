# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# conforme a média atingida:
#
# – Média abaixo de 5,0: REPROVADO
#
# – Média entre 5,0 e 6,9: RECUPERAÇÃO
#
# – Média 7,0 ou superior: APROVADO
nota1 = float(input('Informe a primeira nota '))
nota2 = float(input('Informe a segunda nota '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Parabéns!!! Sua média foi {} você foi aprovado'.format(media))
elif media >= 5 and media <= 6.9:
    print('Atenção!!! Sua média foi {} Você está de recuperação'.format(media))
elif media < 5:
    print('Que pena!!! Sua média foi {} Você reprovou :('.format(media))
