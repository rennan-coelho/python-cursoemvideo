vel = int(input('Digite a velocidade que você estava: '))
vdm = (vel - 80) * 7
if vel > 80:
    print('Você foi multado! e o valor de sua multa será de R${}.00'.format(vdm))
else:
    print('Você estava dentro do limite, parabéns!')    

