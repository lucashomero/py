# =====================================================
# MÓDULOS MAIS USADOS DA BIBLIOTECA PADRÃO — PYTHON
# =====================================================

# 1. datetime — manipulação de datas e horas
import datetime

hoje = datetime.date.today()
print("Hoje é:", hoje)

agora = datetime.datetime.now()
print("Agora:", agora)

# 2. time — controle de tempo e pausas
import time

print("Esperando 2 segundos...")
time.sleep(2)
print("Fim da espera.")

# 3. random — números aleatórios
import random

print(random.randint(1, 10))          # Inteiro aleatório de 1 a 10
print(random.choice(["a", "b", "c"])) # Escolha aleatória
print(random.sample(range(100), 5))   # 5 valores únicos

# 4. os — interação com o sistema operacional
import os

print("Diretório atual:", os.getcwd())
# os.mkdir("nova_pasta")               # Cria nova pasta
# os.remove("arquivo.txt")            # Remove arquivo

# 5. sys — informações do sistema e argumentos
import sys

print("Versão do Python:", sys.version)
print("Argumentos da linha de comando:", sys.argv)

# 6. json — leitura e escrita de JSON
import json

dados = {"nome": "Lucas", "idade": 21}
json_str = json.dumps(dados)            # dict → string JSON
print(json_str)

obj = json.loads(json_str)              # string JSON → dict
print(obj["nome"])

# 7. statistics — operações estatísticas simples
import statistics

valores = [10, 20, 30, 40]
print("Média:", statistics.mean(valores))
print("Mediana:", statistics.median(valores))

# 8. math — funções matemáticas
import math

print("Raiz quadrada de 25:", math.sqrt(25))
print("Fatorial de 5:", math.factorial(5))

# 9. decimal — precisão com casas decimais
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
print(a + b)  # 0.3 com precisão exata

# 10. fractions — frações matemáticas exatas
from fractions import Fraction

f = Fraction(3, 4) + Fraction(1, 4)
print(f)  # 1

# =====================================================
# FIM DO GUIA
# =====================================================
