import random
print('Fale o nome dos alunos: ')
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
altds = [al1, al2, al3, al4]
random.shuffle(altds)
print('e a ordem selecionada foi {} ' .format(altds))








