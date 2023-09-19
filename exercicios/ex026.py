frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posicão {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posicão {}.'.format(frase.rfind('A')+1))
