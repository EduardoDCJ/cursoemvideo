# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    tot_area = largura * comprimento
    print(f'A área do terreno com dimensões de {largura}m x {comprimento}m '
          f'tem um total de {tot_area:.2f}m²')


print(' Cálculo da área do terreno ')
lar = float(input('Largura(m): '))
comp = float(input('Comprimento(m): '))
area(lar, comp)
