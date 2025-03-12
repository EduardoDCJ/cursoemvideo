#Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

metro = float(input("Digite o valor em metros: "))

centimetro = metro * 100
milimetro = metro * 1000

print("A medida {}m convertida para centímetro é igual a {}cm\n"
      "A medida {}m convertida para milimetro é igual a {}mm"
      .format(metro, centimetro, metro, milimetro))
