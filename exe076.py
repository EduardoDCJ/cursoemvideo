# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('lapis', 2.50, 'borracha', 1.80, 'caderno', 12.50, 'mochila', 58, 'estojo', 9.99)
print(f'{"Lista de Produtos":^40}')
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<30}', end='')
    else:
        print(f'R${produtos[p]:.>7.2f}')
