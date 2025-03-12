# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada
# está com os parênteses abertos e fechados na ordem correta.
expressao = str(input('digite '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A quantidade de parenteses é válida!')
else:
    print('A quantidade de parenteses é inválida!')
