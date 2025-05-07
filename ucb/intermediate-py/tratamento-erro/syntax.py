# =====================================================
# TRATAMENTO DE ERROS EM PYTHON — try / except
# =====================================================

# A estrutura try / except permite capturar e tratar erros durante a execução

# -----------------------------------------------------
# 1. Estrutura básica
try:
    # código que pode gerar erro
    x = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero")

# =====================================================
# 2. Capturar erro genérico (não recomendado em produção)
try:
    resultado = int("abc")
except:
    print("Erro ocorreu!")

# =====================================================
# 3. Capturar múltiplos tipos de erro
try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Erro: índice fora do intervalo")
except TypeError:
    print("Erro: tipo incompatível")

# =====================================================
# 4. Usar else (executa se não houver erro)
try:
    numero = int("123")
except ValueError:
    print("Erro: valor inválido")
else:
    print("Conversão bem-sucedida:", numero)

# =====================================================
# 5. Usar finally (executa sempre, com ou sem erro)
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
finally:
    print("Operação finalizada (com ou sem erro)")

# =====================================================
# 6. Levantar um erro manualmente com raise
def dividir(a, b):
    if b == 0:
        raise ValueError("O denominador não pode ser zero")
    return a / b

try:
    print(dividir(10, 0))
except ValueError as e:
    print("Erro personalizado:", e)

# =====================================================
# FIM DO MATERIAL
# =====================================================
