#Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input("Digite a temperatura em Celsius: "))

fahrenheit = temperatura * 1.8 + 32

print("A temperatura {:.1f}°C convertendo para Fahrenheit será igual a {:.1f}°F"
      .format(temperatura, fahrenheit))
