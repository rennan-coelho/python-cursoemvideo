f = input('Digite uma frase: ')
f = f.lower()
ca = f.count('a')
pp = f.find('a') + 1
up = f.rfind('a') + 1
print("A letra 'A' aparece {} vezes na frase." .format(ca))
print("Ela aparece pela primeira vez na posicão {}." .format(pp))
print("Ela aparece pela última vez na posicão {}." .format(up))
