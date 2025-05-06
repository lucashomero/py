# Interpolação
# # %s um string
# %o, %d, %x um número inteiro em octal, decimal ou hexadecimal
# %e um real exponencial
# %f um número real de precisão simples
# %% um único sinal de porcentagem
# 

# Acessando valores
a = "ABCDEF"
a[5] # F
a[2:4] # CD
a[:2] # AB
a[1:] # BCDEF

# Entrada de Usuário
# Recebendo dados de forma dinâmica
# nome = input("Digite um nome: ")
# idade = input("Digite sua idade: ")
# print(f"Seu nome é {nome} e tem {idade} anos")

# Formatando Strings
nome = "Lucas"
idade = 21
print(f"Meu nome é {nome} e tenho {idade} anos.")

# Operações dentro da f-string
print(f"2 + 3 = {2 + 3}")

# Formatando números
pi = 3.14159
print(f"Pi arredondado: {pi:.2f}")       # 2 casas decimais
print(f"Pi científico: {pi:.2e}")        # Notação científica

# Alinhamento e preenchimento
print(f"|{'texto':^10}|")  # centraliza
print(f"|{'esq':<10}|")    # alinha à esquerda
print(f"|{'dir':>10}|")    # alinha à direita

# Preenchendo espaço vazio
preco = 12.53425
print(f"Preco: R${preco:.2f}!")
print(f"Preco: R${preco:.^10.2f}!")
print(f"Preco: R${preco:x^10.2f}!")
print(f"Preco: R${preco:_^10.2f}!")

# Sem printf
nome = "Lucas"
idade = 21
print("Nome:", nome, "Idade:", idade)

# Usando concatenação
idade = 21
print("Idade: " + str(idade))

# Usando .format()
nome = "Lucas"
idade = 21
print("Nome: {}, Idade: {}".format(nome, idade))

# Operadores Lógicos
# a is b - True se a e b são idênticos
# a is not b - True se a e b não são idênticos
# a in b - True se a é membro de b
# a not in b - True se a não é membro de b
# a and b - True se os dois forem
# a or b - False apenas quando os dois são

x = 5.1
print(f"Inteiro: {int(x)}")
print(f"Inteiro: {int(x)*10:5.2f}")