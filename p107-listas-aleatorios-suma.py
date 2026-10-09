# p107-listas-aleatorios-suma.py
# Generar 2 listas de 10 números aleatorios cada una. Crear una tercera lista donde el elemento sea la suma de
# los correspondientes de las listas A y B, solo si AMBOS elementos son impares;
# de lo contrario, el elemento de la tercera lista será 0. Imprimir las 3 listas.
print("\033[2J\033[H", end="")
import random

listaA = [random.randint(1, 100) for _ in range(10)]
listaB = [random.randint(1, 100) for _ in range(10)]
listaC = []

for i in range(10):
    if listaA[i] % 2 == 1 and listaB[i] % 2 == 1:
        listaC.append(listaA[i] + listaB[i])
    else:
        listaC.append(0)

print(f"Lista A: {listaA}")
print(f"Lista B: {listaB}")
print(f"Lista C: {listaC}")