# O mesmo professor do desafio 19 quer sortear a ordem
# de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
alunos = []

for i in range(4):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

random.shuffle(alunos)
print(alunos)
