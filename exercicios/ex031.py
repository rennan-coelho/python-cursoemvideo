dis = float(input('Qual a distância em da viagem? '))
print('Você está prestes a comecar uma viagem de {:.1f}Km'.format(dis))
'''if dis <= 200:
    print('O valor da passagem será de R${:.2f}'.format(dis * 0.50))
else:
    print('O valor da passagem será de R${:.2f}'.format(dis * 0.45))''' 
preco = dis * 0.50 if dis <= 200 else dis * 0.45
print('O valor da passagem será de R${:.2f}'.format(preco))





