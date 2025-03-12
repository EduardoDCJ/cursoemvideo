soma = mais_1000 = barato = cont = 0
nome_barato = ' '
while True:

    nome_produtos = str(input('Informe o nome do produto: '))
    preco_produtos = float(input('Informe o preço do produto R$'))
    cont += 1
    soma += preco_produtos
    if preco_produtos > 1000:
        mais_1000 += 1
    if cont == 1 or preco_produtos < barato:
        barato = preco_produtos
        nome_barato = nome_produtos
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'O total da compra foi de R${soma}')
print(f'{mais_1000} produtos custaram mais de R$1000 reais')
print(f'{nome_barato} foi o produto mais barato da lista custando R${barato}')
