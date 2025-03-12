#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input("Digite o número: "))
d = n * 2
t = n * 3
raiz = n ** 0.5

print("o dobro de {:.0f} é {:.2f}\n"
      "o triplo de {:.0f} é {:.2f}\n"
      "a raiz quadrada de {:.0f} é {:.2f}".format(n, d, n, t, n, raiz))

