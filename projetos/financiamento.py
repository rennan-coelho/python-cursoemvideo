import math
print('Preencha os dados abaixo e saiba qual o valor do seu financiamento.')
vv = float(input('digite o valor a vista do produto: '))
e = float(input('digite quanto deseja dar de entrada: '))
vf = vv - e
n = float(input('Deseja parcelar em quantas vezes: '))
j = float(input('Digite a porcentagem de juros a.m: '))
i = j / 100
prts = (i + 1) ** n
p = vf * prts * i / (prts - 1)
jt = p * 48 - vf
print('O valor das suas {} parcelas, vão ser de R${:.2f} reais por mês.'.format((math.trunc(n)), p))
print('Em {} meses pagando R${:.2f} reais, o juros total será de R${:.2f} reais.' .format(math.trunc(n), p, jt))














