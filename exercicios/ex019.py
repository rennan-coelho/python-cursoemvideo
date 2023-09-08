import random
print('digite os nomes dos alunos: ')
al1 = str(input('Nome do primeiro aluno: '))
al2 = str(input('Nome do segundo aluno: '))
al3 = str(input('Nome do terceiro aluno: '))
al4 = str(input('Nome do quarto aluno: '))
altds = (al1, al2, al3, al4)
alsor = random.choice(altds)
print('Os alunos que vão participar são {} ' .format(altds))
print('O escolhido foi {}' .format(alsor))





