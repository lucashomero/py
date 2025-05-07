# Questão 4
# Verifique se uma string é um palíndromo.
# Ignore espaços, pontuações e maiúsculas/minúsculas.

import string

frase = input("Digite uma palavra ou frase: ")

# Remove espaços, pontuações e converte para minúsculas
frase_limpa = ''.join(
    letra.lower() for letra in frase if letra.isalnum()
)

# Verifica se é igual à versão invertida
if frase_limpa == frase_limpa[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")