import re

def contar_palavras(texto):
    padrao = r'\b\w+\b'
    
    palavras = re.findall(padrao, texto)
    
    palavras = [palavra for palavra in palavras if len(palavra) >= 2 ]
    
    return len(palavras)

# Exemplo de uso:
texto = str(input('Digite o texto: '))
total_palavras = contar_palavras(texto)
print(f"Total de palavras: {total_palavras}")
