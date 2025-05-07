# Questao 2
# 2 Escreva um aplicativo que insere um número consistindo em cinco dígitos
# do usuário, separa o número em seus dígitos individuais e imprime os
# dígitos separados uns dos outros por três espaços cada. Por exemplo, se o
# usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.

numero = input("Digite um numero de 5 digitos:")
if len(numero) == 5 and numero.isdigit():
        resultado = '   '.join(numero)
        print(resultado)
else: 
        print("Erro, digite exatamente 5 digitos numericos")
