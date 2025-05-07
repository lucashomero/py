# =====================================================
# FUNÇÕES EM PYTHON — RESUMO COMPLETO
# =====================================================

# 1. DEFININDO UMA FUNÇÃO
def saudacao():
    print("Olá!")

saudacao()

# 2. FUNÇÃO COM PARÂMETROS
def exibir_nome(nome):
    print("Nome:", nome)

exibir_nome("Lucas")

# 3. FUNÇÃO COM RETORNO
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Resultado:", resultado)

# 4. PARÂMETROS COM VALOR PADRÃO
def boas_vindas(nome="visitante"):
    print(f"Bem-vindo, {nome}!")

boas_vindas()
boas_vindas("Homero")

# 5. *ARGS — PARÂMETROS VARIÁVEIS (TUPLA)
def somar_tudo(*numeros):
    return sum(numeros)

print(somar_tudo(1, 2, 3, 4))

# 6. **KWARGS — PARÂMETROS NOMEADOS VARIÁVEIS (DICIONÁRIO)
def mostrar_dados(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Lucas", idade=21)

# 7. FUNÇÕES ANINHADAS
def externa():
    def interna():
        print("Função interna chamada")
    interna()

externa()

# 8. FUNÇÕES LAMBDA (ANÔNIMAS)
dobro = lambda x: x * 2
print(dobro(4))

# 9. DOCSTRING — DOCUMENTAÇÃO DA FUNÇÃO
def exemplo():
    """Esta função é apenas um exemplo."""
    return True

print(exemplo.__doc__)

# 10. PASS — FUNÇÃO AINDA NÃO IMPLEMENTADA
def ainda_nao_feita():
    pass

# =====================================================
# FIM DO RESUMO
# =====================================================
