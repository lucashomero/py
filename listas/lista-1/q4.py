# 4 Crie um programa que peça ao usuário para digitar uma frase e conte
# quantas vogais (a, e, i, o, u) aparecem na frase. Considere que a contagem
# deve ser case-insensitive (ou seja, não diferencie maiúsculas de
# minúsculas).

frase = input("Digite uma frase: ")
contador = 0

for letra in frase.lower():
    if letra in "aeiou":
        contador += 1

print(contador)


# frase.lower() garante o insentive-case
# in em Python serve para verificar se um valor esta contido em algo