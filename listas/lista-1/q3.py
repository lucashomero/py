# 3 Faça um programa que calcule a distância entre dois pontos no plano
# cartesiano .
# d1,2 = math.sqrt((x − x )**2 + (y − y )**2) 

import math

def ler_cordenada(nome): 
    while True:
        valor = input(f"Digite a posiçao de {nome}: ")
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        else:
            print("Digite um número válido maior que zero")

x1 = ler_cordenada("x1")
x2 = ler_cordenada("x2")
y1 = ler_cordenada("y1")
y2 = ler_cordenada("y2")

def calcular_distancia(x1,x2,y1,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

distancia = calcular_distancia(x1, x2, y1, y2)
print(distancia)