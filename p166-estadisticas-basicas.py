# p166-estadisticas-basicas.py
# Crea un programa que calcule estadísticas básicas (poblacionales) para una lista de números. El programa debe incluir:
# 1. Una función para leer una lista de números enteros.
# 2. Funciones separadas para calcular y devolver cada una de las siguientes estadísticas:
def leer_lista():
    numeros = input("Dame los números (separados por espacio): ")
    lista = [int(num) for num in numeros.split()]
    return lista
def mayor(lista):
    return max(lista)
def menor(lista):
    return min(lista)
def media(lista):
    return sum(lista) / len(lista)
def varianza(lista):
    m = media(lista)
    return sum((x - m) ** 2 for x in lista) / len(lista)
def desviacion_estandar(lista):
    return varianza(lista) ** 0.5

# Programa principal
numeros = leer_lista()
print("La lista de números original          :", numeros)
print("Estadistica")
print("Mayor número        :", mayor(numeros))
print("Menor número        :", menor(numeros))
print("Media               :", media(numeros))
print("Varianza            :", varianza(numeros))
print("Desviación estándar :", desviacion_estandar(numeros))