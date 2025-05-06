# Solicita um número de 5 dígitos ao usuário
numero = input("Digite um número de 5 dígitos: ")

# Verifica se o número tem exatamente 5 dígitos
if len(numero) == 5 and numero.isdigit():
    # Junta os dígitos com 3 espaços entre eles
    resultado = '   '.join(numero)
    print(resultado)
else:
    print("Por favor, digite exatamente 5 dígitos numéricos.")
