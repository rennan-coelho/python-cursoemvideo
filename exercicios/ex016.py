dias = float(input('Quantidade de dias que ficou com o veiculo: '))
km = float(input('Quantidade de km percorridos: '))
pago = (dias * 60) + (km * 0.15)
print('Você ficou com o veiculo por {:.0f} dias, e percorreu {}km.\nResultando em um valor de R${:.2f}'.format(dias,km,pago))

