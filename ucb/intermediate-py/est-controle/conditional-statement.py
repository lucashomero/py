# =====================================================
# CONDICIONAIS, STATEMENTS E OPERADORES

# 1. IF / ELIF / ELSE
idade = 18

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("Maior de idade")

# 2. OPERADORES DE COMPARAÇÃO
# ==  igual
# !=  diferente
# >   maior
# <   menor
# >=  maior ou igual
# <=  menor ou igual

a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a < b)   # True

# 3. OPERADORES LÓGICOS
# and → True se ambas forem verdadeiras
# or  → True se pelo menos uma for verdadeira
# not → inverte o valor

x = 5
y = 10

if x > 2 and y > 5:
    print("Ambas condições verdadeiras")

if x > 10 or y > 5:
    print("Pelo menos uma é verdadeira")

if not x > 10:
    print("x NÃO é maior que 10")

# 4. STATEMENTS ÚTEIS

# pass → usado como placeholder (não faz nada)
if True:
    pass  # evita erro de indentação

# continue → pula para a próxima iteração
for i in range(5):
    if i == 2:
        continue
    print(i)  # pula o 2

# break → interrompe o loop
for i in range(5):
    if i == 3:
        break
    print(i)  # para no 2

# 5. OPERADOR TERNÁRIO (condição em 1 linha)
idade = 20
status = "maior" if idade >= 18 else "menor"
print(status)
