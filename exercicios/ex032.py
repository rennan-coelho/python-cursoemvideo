from datetime import date
ano = int(input('Qual ano deseja analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Analisar o ano atual configurado na maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} não é um ano BISSEXTO!'.format(ano))
    

    