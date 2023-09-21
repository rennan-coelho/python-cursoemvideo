sa = float(input('Digite o valor atual do seu salário: R$'))
if sa <= 1250:
    aum1 = sa + (sa*0.15)
    print('Seu salário agora será dde R${:.2f}'.format(aum1))
else:
    aum2 = sa + (sa*0.10)
    print('Seu salá agora será de R${:.2f}'.format(aum2))


    
