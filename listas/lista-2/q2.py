# Questão 2
# Escreva um aplicativo que solicita ao usuário que insira o tamanho do lado de um quadrado (1 a 20)
# e exiba um quadrado vazio desse tamanho usando asteriscos.

lado = int(input("Digite o tamanho do lado do quadrado (1 a 20): "))

if 1 <= lado <= 20:
    for i in range(lado):
        if i == 0 or i == lado - 1:
            print("*" * lado)  # primeira e última linha cheias de asteriscos
        else:
            print("*" + " " * (lado - 2) + "*")  # linhas do meio com espaço no centro
else:
    print("Tamanho inválido. Digite um valor entre 1 e 20.")