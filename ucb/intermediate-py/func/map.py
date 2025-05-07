# =====================================================
# FUNÇÃO map() EM PYTHON — RESUMO
# =====================================================

# A função map() aplica uma função a cada item de um iterável
# e retorna um iterador com os resultados.

# Sintaxe:
# map(função, iterável)

# Para ver os resultados, geralmente convertemos com list()

# =====================================================
# 1. Exemplo básico: dobrar valores
numeros = [1, 2, 3, 4]

dobrados = map(lambda x: x * 2, numeros)
print(list(dobrados))  # [2, 4, 6, 8]

# =====================================================
# 2. Converter Celsius para Fahrenheit
celsius = [0, 10, 20, 30]

fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))  # [32.0, 50.0, 68.0, 86.0]

# =====================================================
# 3. Colocar todos os nomes em maiúsculo
nomes = ["ana", "joão", "bia"]

maiusculas = map(lambda nome: nome.upper(), nomes)
print(list(maiusculas))  # ['ANA', 'JOÃO', 'BIA']

# =====================================================
# 4. Arredondar preços para 2 casas decimais
precos = [29.987, 9.951, 14.509]

precos_corrigidos = map(lambda p: round(p, 2), precos)
print(list(precos_corrigidos))  # [29.99, 9.95, 14.51]

# =====================================================
# 5. Usar função definida ao invés de lambda
def quadrado(x):
    return x ** 2

valores = [2, 3, 4]
resultado = map(quadrado, valores)
print(list(resultado))  # [4, 9, 16]

# =====================================================
# NOTA: map() retorna um objeto iterador (lazy)
# Se quiser reutilizar, é necessário converter com list()
# =====================================================
