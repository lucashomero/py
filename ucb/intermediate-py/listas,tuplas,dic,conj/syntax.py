# Lista
a_list = [1, 2, 3, 4, 5, 6]  # Cria uma lista com 6 elementos
a_list[0]      # Acessa o primeiro elemento (índice 0)
a_list[-1]     # Acessa o último elemento da lista
a_list[0:3]    # Retorna os elementos de índice 0 até 2 (não inclui o índice 3 → [1, 2, 3])
a_list[:3]     # Igual ao acima, omite o índice inicial (assume 0)
a_list[2:]     # Retorna do índice 2 até o final da lista → [3, 4, 5, 6]
a_list[::2]    # Retorna elementos com passo 2 → [1, 3, 5]
a_list[:]  # retorna toda a lista

# ////////////////////////////////////////////////////////////////////

# Dicionarios
# Criar um dicionário com IDs e preços
precos = {
    101: 29.90,
    102: 49.99,
    103: 10.50,
    104: 99.00
}
# Acessar o preço de um produto específico pelo ID
precos[101]            # Retorna: 29.90
# Adicionar um novo produto com preço
precos[105] = 15.00
# Atualizar o preço de um produto
precos[102] = 45.99
# Remover um produto
del precos[104]
# Verificar se um produto_id existe
102 in precos          # Retorna: True
999 in precos          # Retorna: False
# Obter todos os IDs de produtos
precos.keys()          # dict_keys([101, 102, 103, 105])
# Obter todos os preços
precos.values()        # dict_values([29.90, 45.99, 10.50, 15.00])
# Obter todos os pares produto_id:preço
precos.items()         # dict_items([(101, 29.90), (102, 45.99), ...])
# Iterar sobre todos os produtos
for produto_id, preco in precos.items():
    print(f"Produto {produto_id}: R${preco:.2f}")
# Obter um preço com segurança
precos.get(999)        # Retorna: None
precos.get(999, 0.0)   # Retorna: 0.0 (valor padrão)

# ////////////////////////////////////////////////////////////////////

# tuple (Tupla)

# Estrutura imutável (não pode ser alterada).
# Pode conter valores de qualquer tipo.
# Suporta indexação e slicing, assim como listas.
# Criar uma tupla
tupla = (10, 20, 30)
# Acessar elementos
tupla[0]         # 10
tupla[-1]        # 30
# Slicing
tupla[1:]        # (20, 30)
# Tupla com 1 elemento (atenção à vírgula)
tupla1 = (42,)   # Não é só um número — é uma tupla!
# Iterar sobre uma tupla
for item in tupla:
    print(item)
# Verificar se um item está na tupla
20 in tupla      # True

# ////////////////////////////////////////////////////////////////////

# set (Conjunto)

# Não aceita valores duplicados
# Desordenado (sem índice)
# Muito útil para operações matemáticas como união, interseção, etc.
# Criar um set
conjunto = {1, 2, 3, 2, 1}
print(conjunto)     # {1, 2, 3} → duplicatas são eliminadas
# Adicionar elementos
conjunto.add(4)
# Remover elementos
conjunto.remove(2)  # Erro se não existir
conjunto.discard(5) # Sem erro se não existir
# Verificar existência
3 in conjunto       # True
# União
a = {1, 2}
b = {2, 3}
a | b               # {1, 2, 3}
# Interseção
a & b               # {2}
# Diferença
a - b               # {1}
# Iterar
for item in conjunto:
    print(item)


# Lista → Conjunto (set)
# Remove duplicatas automaticamente.
lista = [1, 2, 2, 3, 4, 4]
conjunto = set(lista)
print(conjunto)  # Saída: {1, 2, 3, 4}

# Conjunto → Lista (list)
# Recria uma lista (a ordem pode não ser garantida).
conjunto = {1, 2, 3}
lista = list(conjunto)
print(lista)  # Saída: [1, 2, 3] (ou em outra ordem)

# =====================================================

# COMPARATIVO DE COLEÇÕES EM PYTHON

# | Tipo     | Sintaxe                | Mutável | Duplicados | Ordenado | Usa Chaves |
# |----------|------------------------|---------|------------|----------|------------|
# | list     | [1, 2, 3]              | Sim     | Sim        | Sim      | Não        |
# | tuple    | (1, 2, 3)              | Não     | Sim        | Sim      | Não        |
# | set      | {1, 2, 3}              | Sim     | Não        | Não      | Não        |
# | dict     | {"a": 1, "b": 2}       | Sim     | Não*       | Sim**    | Sim        |
