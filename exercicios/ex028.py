import random
n =  int(input('Tente adivinhar um número de 0 a 5: '))
ni = (0, 1, 2, 3, 4, 5)
ne = random.choice(ni)
if ne == n:
    print('Parabens você acertou, o número correto foi {}!'.format(ne))
else:
    print('Que pena você errou, o número correto seria {}' .format(ne))    

