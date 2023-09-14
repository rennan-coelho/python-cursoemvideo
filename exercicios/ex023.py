n = int(input('Digite um número de 0 a 9999: '))
if 0 <= n <= 9999:
    u = n % 10
    d = (n // 10) % 10
    c = (n // 100) % 10
    m = (n // 1000) % 10

    print('Unidade: ', u)
    print('dezena: ', d)   
    print('Centena: ', c)
    print('Milhar: ', m)

else: 
    print('Número fora do intervalo válido.')
        


