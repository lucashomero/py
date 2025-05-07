# Questão 1
# Crie um programa que some todos os números pares entre 1 e N, onde N é fornecido pelo usuário.

print("Descubra a soma de todos os numeros pares entre 1 e N")
numero = int(input("digite o valor de N: "))
soma_pares = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        soma_pares += i

print (soma_pares)

