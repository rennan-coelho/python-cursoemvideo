sa = float(input('Digite o valor atual do seu salário: R$'))
if sa <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sa, sa + (sa*0.15)))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(sa, sa + (sa*0.10)))
    



    
