cidade = input('Digite o nome da cidade: ')
cidade = cidade.strip().lower()

if cidade[:5] == 'santo':
    print("O nome da cidade comeca com 'Santo'.")
else:
    print("O nome da cidade não comeca com 'Santo'.")
    