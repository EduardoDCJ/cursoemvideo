# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos
# e escrevendo na tela o nome do escolhido.
import random
alunos = []

for i in range(4):
    nome = input("O nome do aluno: ")
    alunos.append(nome)

apagador = random.choice(alunos)

print(f"O aluno escolhido para apagar o quadro foi {apagador}")
