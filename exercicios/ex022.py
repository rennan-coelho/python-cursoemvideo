nome = input('Digite seu nome completo: ')
ma = nome.upper()
mi = nome.lower()
tl = len(nome.replace(' ', ''))
pn = nome.split()
pnm = pn[0]
ldp = len(pnm)
print('Nome em maiúsculas: {}' .format(ma))
print('Nome em minúsculas: {}' .format(mi))
print('Total de letras (sem espacos): {}' .format(tl))
print('Letras no primeiro nome: {}' .format(ldp))

