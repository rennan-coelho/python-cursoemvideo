import math
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O seno de {} é : {:.2f}'.format(an, sen))
print('O cosseno de {} é: {:.2f}'.format(an, cos))
print('A tangente de {} é: {:.2f}'.format(an, tan))
