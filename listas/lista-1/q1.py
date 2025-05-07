# 1 Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um losango utilizando asteriscos (*)
# Caixa
print("Caixa:")
for i in range(5):
    if i == 0 or i == 4:
        print("*" * 9)
    else:
        print("*" + " " * 7 + "*")
print()

# Oval (forma fixa com laços parciais)
print("Oval:")
oval = [
    "   ***   ",
    " *     * ",
    "*       *",
    " *     * ",
    "   ***   "
]
for linha in oval:
    print(linha)
print()

# Seta
print("Seta:")
for i in range(3):
    print(" " * (2 - i) + "*" * (2 * i + 1))  # topo da seta
for _ in range(4):
    print("  *")  # haste
print()

# Losango
print("Losango:")
altura = 7
meio = altura // 2

# Parte superior
for i in range(meio + 1):
    espacos = " " * (meio - i)
    if i == 0:
        print(espacos + "*")
    else:
        print(espacos + "*" + " " * (2 * i - 1) + "*")

# Parte inferior
for i in range(meio - 1, -1, -1):
    espacos = " " * (meio - i)
    if i == 0:
        print(espacos + "*")
    else:
        print(espacos + "*" + " " * (2 * i - 1) + "*")
