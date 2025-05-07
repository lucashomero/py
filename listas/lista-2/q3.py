# Questão 3
# Crie um jogo de adivinhação onde o programa escolhe um número aleatório entre 1 e 100
# e o usuário precisa adivinhar qual é o número.

import random

numero = random.randint(1, 100)
print(f"{numero}")

chute = int(input("Chute um numero no intervalo entre 1 e 100: "))

while chute != numero:
    if chute > numero:
        print("O chute é maior que o numero escolhido. Tente novamente")
        chute = int(input("Chute um numero no intervalo entre 1 e 100: "))
    elif chute < numero:
        print("O chute é menor que o numero escolhido. Tente novamente")
        chute = int(input("Chute um numero no intervalo entre 1 e 100: "))

print(f"Voce acertou o numero é {numero}")
