# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km = float(input("informe a quantidade de km rodados: "))
dias = int(input("Informe a quantidade de dias alugado: "))

custo = (km * 0.15) + (dias * 60)

print("O valor total a pagar pelo aluguel do veiculo será de R${:.2f}".format(custo))
