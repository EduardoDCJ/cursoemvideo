# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# Minha solução
palavras = ('python', 'curso', 'em', 'video')
for letra in range(len(palavras)):
    if 'a' in palavras[letra]:
        print(f'{palavras[letra]} possui letra "a" ', end='')
    if 'e' in palavras[letra]:
        print(f'{palavras[letra]} possui letra "e" ', end='')
    if 'i' in palavras[letra]:
        print(f'{palavras[letra]} possui letra "i" ', end='')
    if 'o' in palavras[letra]:
        print(f'{palavras[letra]} possui letra "o" ', end='')
    if 'u' in palavras[letra]:
        print(f'{palavras[letra]} possui letra "u" ')
    print('\n')
# solução guanabara
for p in palavras:
    print(f'na palavra {p} temos ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
    print('\n')
