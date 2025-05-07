# =====================================================
# FUNÇÕES LAMBDA

# Função lambda = função anônima (sem nome)
# Sintaxe:
# lambda argumentos: expressão

# -----------------------------------------------------
# 1. Exemplo básico
soma = lambda x, y: x + y
print(soma(3, 4))  # 7

# -----------------------------------------------------
# 2. Lambda com map (aplica uma função a cada item de uma lista)
numeros = [1, 2, 3, 4]
dobros = list(map(lambda x: x * 2, numeros))
print(dobros)  # [2, 4, 6, 8]

# -----------------------------------------------------
# 3. Lambda com filter (filtra itens com base em uma condição)
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# -----------------------------------------------------
# 4. Lambda com sorted e chave personalizada
nomes = ["ana", "joao", "bia", "carlos"]
ordenado = sorted(nomes, key=lambda nome: len(nome))
print(ordenado)  # ['ana', 'bia', 'joao', 'carlos']

# -----------------------------------------------------
# 5. Equivalente a função normal
def quadrado(x):
    return x * x

# Lambda equivalente
quadrado_lambda = lambda x: x * x

print(quadrado(5))        # 25
print(quadrado_lambda(5)) # 25

# =====================================================
# LIMITAÇÃO: só pode ter uma única expressão (sem múltiplas linhas)
# USO: comum em funções rápidas, callbacks e código funcional
# =====================================================

# =====================================================
# map() COM FUNÇÕES LAMBDA 
# =====================================================

# map() aplica uma função a cada item de um iterável e retorna um iterador.
# Sintaxe: map(função, iterável)

# -----------------------------------------------------
# 1. Dobrar os valores de uma lista
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print("Dobro:", dobrados)  # [2, 4, 6, 8, 10]

# -----------------------------------------------------
# 2. Converter Celsius para Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Temperaturas em Fahrenheit:", fahrenheit)  # [32.0, 50.0, 68.0, 86.0]

# -----------------------------------------------------
# 3. Deixar nomes em maiúsculo
nomes = ["ana", "joão", "bia"]
maiusculas = list(map(lambda nome: nome.upper(), nomes))
print("Nomes em maiúsculo:", maiusculas)  # ['ANA', 'JOÃO', 'BIA']

# =====================================================
# filter() COM FUNÇÕES LAMBDA 
# =====================================================

# filter() seleciona os itens que satisfazem uma condição (função retorna True)
# Sintaxe: filter(função, iterável)

# -----------------------------------------------------
# 1. Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)  # [2, 4, 6]

# -----------------------------------------------------
# 2. Filtrar nomes com mais de 3 letras
nomes = ["Ana", "João", "Bia", "Carlos"]
longos = list(filter(lambda nome: len(nome) > 3, nomes))
print("Nomes longos:", longos)  # ['João', 'Carlos']

# -----------------------------------------------------
# 3. Filtrar temperaturas abaixo de 20 graus
temperaturas = [15, 22, 19, 30, 18]
frias = list(filter(lambda t: t < 20, temperaturas))
print("Temperaturas frias:", frias)  # [15, 19, 18]

# =====================================================
# FIM DO MATERIAL
# =====================================================
