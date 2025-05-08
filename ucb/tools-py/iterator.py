# Iteráveis vs Iteradores em Python

# --------------------------
# Iterável (Iterable)
# --------------------------
# Um iterável é um objeto que pode ser percorrido com um loop for.
# Exemplos de iteráveis: list, tuple, str, dict, set, range, etc.
# Um iterável possui o método __iter__().
# Pode ser convertido em um iterador usando a função iter().

# Exemplo:
lista = [1, 2, 3]           # lista é um iterável
iterador = iter(lista)      # agora temos um iterador a partir da lista

# --------------------------
# Iterador (Iterator)
# --------------------------
# Um iterador é um objeto que permite percorrer os valores de um iterável, um por um.
# Ele mantém o estado da iteração e possui os métodos __iter__() e __next__().
# A função next() retorna o próximo valor do iterador.
# Quando os valores acabam, uma exceção StopIteration é lançada.

# Exemplo:
numeros = iter([10, 20, 30])  # iterador criado a partir de uma lista

print(next(numeros))  # 10
print(next(numeros))  # 20
print(next(numeros))  # 30
# print(next(numeros))  # StopIteration (se descomentar, ocorre erro)

# --------------------------
# Verificação com hasattr()
# --------------------------
# Podemos verificar se um objeto é iterável ou iterador usando hasattr():

# Verifica se é iterável
print(hasattr(lista, '__iter__'))    # True
print(hasattr(lista, '__next__'))    # False

# Verifica se é iterador
print(hasattr(iterador, '__iter__')) # True
print(hasattr(iterador, '__next__')) # True