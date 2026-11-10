# p158-aleatorios.py
# funcion para genera lista de numeros aleatorios 
# luego generar 2 listas aleatorias usando esa funcion
# obtengo la suma de ambas con otra funcion
import random

def generar_lista_aleatoria(n: int, min: int, max: int) -> list[int]:
    lista = []
    for _ in range(n):
        numero_aleatorio = random.randint(min, max)
        lista.append(numero_aleatorio)
    return lista
def sumarlistas(lista1: list[int], lista2: list[int]) -> list[int]:
    if len(lista1) != len(lista2):
        return 0
    suma = []
    for i in range(len(lista1)):
        suma.append(lista1[i] + lista2[i])
    return suma
# programa principal
max = 10
lista1 = generar_lista_aleatoria(max, 1, 10)
lista2 = generar_lista_aleatoria(max, 50, 100)
lista3 = sumarlistas(lista1, lista2)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
if lista3 != 0:
    print(f"Suma de ambas listas: {lista3}")
    