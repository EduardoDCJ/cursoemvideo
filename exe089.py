# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que
# o usuário possa mostrar as notas de cada aluno individualmente.
alunos = list()
dados = list()

while True:
    nome = str(input('Aluno: '))
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    dados.append(nome)
    dados.append(n1)
    dados.append(n2)
    alunos.append(dados[:])
    dados.clear()
    resp = input('Deseja adicionar mais algum aluno?[s/n] ')
    if resp != 's':
        break
print(f'{"Nº":<2}{"NOME":^10}{"MÉDIA":>6}')
for a in range(len(alunos)):
    print(f'{a:<2}{alunos[a][0]:^10}{(alunos[a][1]+alunos[a][2])/2:>6.1f}')
while True:
    opc = int(input('Mostrar nota de qual aluno? '))
    if opc > len(alunos):
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) - 1:
        print(f'O aluno {alunos[opc][0]} teve as notas {alunos[opc][1]} {alunos[opc][2]}')
