from random import choice 
from time import sleep # Biblioteca de tempo
n =  int(input('Tente adivinhar um número de 0 a 5: ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2) # Faz o programa passarum tempo "processando"
ni = (0, 1, 2, 3, 4, 5) # Números que o computador irá "PENSAR"
ne = choice(ni) # Faz o computador "PENSAR"
if ne == n:
    print('Parabens você acertou, o número correto foi {}!'.format(ne))
else:
    print('Que pena você errou, o número correto seria {}' .format(ne))  



