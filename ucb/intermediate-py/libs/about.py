# =====================================================
# BIBLIOTECAS E PACOTES EM PYTHON — RESUMO
# =====================================================

# 1. O QUE SÃO

# - Módulo: arquivo `.py` com funções, classes ou variáveis.
# - Biblioteca (lib): conjunto de módulos prontos para uma finalidade (ex: `math`, `json`, `random`).
# - Pacote (package): estrutura de diretórios com vários módulos e um `__init__.py`.

# -----------------------------------------------------
# 2. IMPORTANDO

# Módulo simples
import math
print(math.sqrt(25))

# Apenas parte do módulo
from math import pi
print(pi)

# Módulo renomeado
import math as m
print(m.ceil(2.1))

# -----------------------------------------------------
# 3. INSTALANDO PACOTES EXTERNOS

# No terminal:
# pip install nome_do_pacote

# Exemplo:
# pip install requests

import requests
r = requests.get("https://httpbin.org/get")
print(r.status_code)

# -----------------------------------------------------
# 4. ESTRUTURA DE PACOTE PERSONALIZADO

# my_package/
# ├── __init__.py       # Torna o diretório um pacote
# ├── modulo1.py
# └── modulo2.py

# No script principal:
# from my_package import modulo1
# modulo1.minha_funcao()

# -----------------------------------------------------
# 5. VERIFICAR PACOTES INSTALADOS

# No terminal:
# pip list

# Versão de um pacote específico:
# pip show requests

# Atualizar um pacote:
# pip install --upgrade requests

# Remover um pacote:
# pip uninstall requests

# -----------------------------------------------------
# 6. INSTALAR PACOTES DE REQUISITOS

# Criar arquivo:
# pip freeze > requirements.txt

# Instalar tudo de requirements.txt:
# pip install -r requirements.txt

# =====================================================
# FIM DO RESUMO
# =====================================================
