#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Insira a largura da parede: "))
altura = float(input("Insira a altura da pared: "))

area = largura * altura

litros = area / 2

print("Sabendo que a altura e largura da parede são respectivamente {}m {}m\n"
      "a área total da parede é {}m² e será necessário {}L de tinta para pintá-la".
      format(altura, largura, area, litros))
