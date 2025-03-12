#Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

preco = float(input("Insira o preço do produto: "))

novo_preco = preco - (preco * 5 / 100)

print(novo_preco)