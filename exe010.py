#Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar.

valor = float(input("Digite o saldo: "))

c_d = valor / 5.14

print("Convertendo o saldo R${} para dólar\n"
      "terá saldo igual a {:.1f}".format(valor, c_d))
