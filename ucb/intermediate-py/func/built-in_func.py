# =====================================================
# PYTHON BUILT-IN FUNCTIONS — RESUMO RÁPIDO
# =====================================================

# len() — retorna o tamanho (número de itens)
len("Python")                # 6
len([1, 2, 3])               # 3

# type() — retorna o tipo do objeto
type(3.14)                   # <class 'float'>

# str(), int(), float(), bool() — conversões
str(123)                     # "123"
int("10")                    # 10
float("3.14")                # 3.14
bool("")                     # False

# print() — imprime no console
print("Olá, mundo!")

# input() — lê dados do usuário (como string)
# nome = input("Digite seu nome: ")

# sum() — soma todos os elementos de um iterável
sum([1, 2, 3])               # 6

# max(), min() — retorna o maior e o menor valor
max([1, 5, 3])               # 5
min([1, 5, 3])               # 1

# sorted() — retorna uma nova lista ordenada
sorted([3, 1, 2])            # [1, 2, 3]

# range() — gera uma sequência de números
list(range(5))               # [0, 1, 2, 3, 4]
list(range(1, 10, 2))        # [1, 3, 5, 7, 9]

# enumerate() — retorna índices e valores
for i, v in enumerate(['a', 'b']):
    print(i, v)              # 0 a | 1 b

# zip() — combina elementos de iteráveis
list(zip([1, 2], ['a', 'b']))  # [(1, 'a'), (2, 'b')]

# map() — aplica uma função a todos os itens
list(map(str, [1, 2, 3]))    # ['1', '2', '3']

# filter() — filtra itens com base em uma função
list(filter(lambda x: x > 2, [1, 2, 3, 4]))  # [3, 4]

# any(), all()
any([False, True, False])    # True (algum é True)
all([True, True])            # True (todos são True)

# help() — mostra a documentação da função
# help(len)

# =====================================================
# FUNÇÕES MATEMÁTICAS EM PYTHON

# Built-in functions

# abs() → valor absoluto (sem sinal)
print(abs(-10))         # 10

# pow(x, y) → x elevado à potência y
print(pow(2, 3))        # 8

# divmod(x, y) → retorna (quociente, resto)
print(divmod(10, 3))    # (3, 1)

# round() → arredondamento (visto antes)
print(round(2.675, 2))  # 2.67 (Python usa "round half to even")

# max(), min(), sum() → maiores, menores, soma de iteráveis
print(max([3, 7, 1]))   # 7
print(min([3, 7, 1]))   # 1
print(sum([3, 7, 1]))   # 11

# =====================================================
# Módulo math (import necessário)

import math

# math.sqrt(x) → raiz quadrada
print(math.sqrt(16))    # 4.0

# math.floor(x) → arredonda para baixo
print(math.floor(2.9))  # 2

# math.ceil(x) → arredonda para cima
print(math.ceil(2.1))   # 3

# math.pi → constante π
print(math.pi)          # 3.141592...

# math.e → constante e (Euler)
print(math.e)           # 2.718281...

# math.pow(x, y) → x elevado a y (float)
print(math.pow(2, 3))   # 8.0

# math.log(x[, base]) → logaritmo
print(math.log(8, 2))   # 3.0

# math.fabs(x) → valor absoluto (sempre float)
print(math.fabs(-5))    # 5.0

# =====================================================

