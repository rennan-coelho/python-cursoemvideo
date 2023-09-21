dis = float(input('Qual a distância em Km: '))
if dis <= 200:
    vl = dis * 0.50
    print('O valor a pagar será de R${:.2f}'.format(vl))
else:
    vl2 = dis * 0.45
    print('O valor a pagar será de R${:.2f}'.format(vl2))    
