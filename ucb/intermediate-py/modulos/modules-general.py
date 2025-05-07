# =====================================================
# MÓDULOS EM PYTHON — RESUMO
# =====================================================

# 1. IMPORTANDO MÓDULOS BUILT-IN (INTERNOS)

import math             # Importa todo o módulo
print(math.sqrt(16))    # 4.0

from math import pi     # Importa só pi
print(pi)               # 3.1415...

from math import *      # Importa tudo (não recomendado em projetos grandes)

# Renomeando módulo
import math as m
print(m.ceil(2.3))      # 3

# -----------------------------------------------------

# 2. CRIANDO UM MÓDULO PRÓPRIO

# Arquivo: meu_modulo.py
def saudacao(nome):
    return f"Olá, {nome}!"

# No script principal:
# import meu_modulo
# print(meu_modulo.saudacao("Lucas"))

# -----------------------------------------------------

# 3. USANDO MÓDULOS EXTERNOS (EX: `requests`, `pandas`, etc.)

# Instalar com pip (no terminal):
# pip install nome_do_modulo

# Exemplo:
# pip install requests

import requests
response = requests.get("https://httpbin.org/get")
print(response.status_code)

# -----------------------------------------------------

# 4. VER TODOS OS NOMES DISPONÍVEIS EM UM MÓDULO
import math
print(dir(math))  # Lista todas as funções/atributos do módulo

# 5. VER DOCUMENTAÇÃO DE UMA FUNÇÃO/MÓDULO
help(math.sqrt)

# =====================================================
# FIM DO RESUMO
# =====================================================
