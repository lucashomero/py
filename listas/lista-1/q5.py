# 5 - Uma empresa que quer enviar dados pela internet pediu-lhe que
# escrevesse um programa que criptografe dados a fim de que eles possam
# ser transmitidos com maior segurança. 
# Todos os dados são transmitidos como inteiros de quatro dígitos.
# Seu aplicativo deve ler um inteiro de quatro dígitos inserido pelo usuário e criptografá-lo da seguinte maneira: 
# substitua cada dígito pelo resultado da adição de 7 ao dígito, obtendo o restante depois da divisão do novo valor por 10.
# Troque então o primeiro dígito pelo terceiro e o segundo dígito pelo quarto. 
# Então, imprima o inteiro criptografado. 
# Escreva um aplicativo separado que receba a entrada de um inteiro de quatro dígitos criptografado e o descriptografe (revertendo o
# esquema de criptografia) para formar o número original.

numero = input("Digite um numero de 4 digitos: ")

if numero.isdigit() and len(numero) == 4:
    d1 = (int(numero[0]) + 7) % 10   
    d2 = (int(numero[1]) + 7) % 10   
    d3 = (int(numero[2]) + 7) % 10   
    d4 = (int(numero[3]) + 7) % 10
    
    criptografado = f"{d3}{d4}{d1}{d2}"

    print("Numero criptografado: ", criptografado)
else: 
    print("Digite um numero de 4 digitos valido")

if criptografado.isdigit() and len(criptografado) == 4:
    # Etapa 1: inverter a troca feita na criptografia
    d3 = int(criptografado[0])
    d4 = int(criptografado[1])
    d1 = int(criptografado[2])
    d2 = int(criptografado[3])

    # Etapa 2: aplicar fórmula reversa
    o1 = (d1 + 10 - 7) % 10
    o2 = (d2 + 10 - 7) % 10
    o3 = (d3 + 10 - 7) % 10
    o4 = (d4 + 10 - 7) % 10

    # Montar número original
    original = f"{o1}{o2}{o3}{o4}"
    print("Número original:", original)
else:
    print("Número criptografado inválido.")