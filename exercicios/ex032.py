ano = int(input('Digite uma ano aqui, para saber se ele é bissexto ou não: '))
bi = ano % 4
if bi == 0:
    print('{} é um ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))    
    