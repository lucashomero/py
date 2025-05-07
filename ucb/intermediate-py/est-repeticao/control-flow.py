# =====================================================
# FOR 

# 1. FOR COM LISTA
nomes = ["Lucas", "Ana", "João"]

for nome in nomes:
    print("Olá,", nome)

# 2. FOR COM RANGE
# range(início, fim, passo)
for i in range(5):  # de 0 até 4
    print(i)

for i in range(1, 10, 2):  # de 1 até 9, pulando de 2 em 2
    print(i)

# 3. FOR COM STRING
texto = "Python"

for letra in texto:
    print(letra)

# 4. FOR COM DICIONÁRIO
pessoa = {"nome": "Lucas", "idade": 21}

for chave in pessoa:
    print(chave, "→", pessoa[chave])

# ou usando .items()
for chave, valor in pessoa.items():
    print(chave, ":", valor)

# 5. FOR COM ENUMERATE
frutas = ["maçã", "banana", "uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# 6. FOR COM LIST COMPREHENSION
quadrados = [x**2 for x in range(1, 6)]
print(quadrados)  # [1, 4, 9, 16, 25]

# 7. FOR COM CONDIÇÃO (LIST COMPREHENSION FILTRADA)
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# =====================================================
# SINTAXE BÁSICA DO FOR LOOP EM PYTHON
# =====================================================

# for variável in iterável:
#     bloco_de_código

# -----------------------------------------------------
# variável       → nome que você escolhe para representar cada item da sequência
# iterável       → objeto que pode ser percorrido item por item (ex: lista, string, range, tupla, dicionário)
# bloco_de_código → o que será executado a cada iteração (deve estar identado)

