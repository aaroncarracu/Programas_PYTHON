# p102-aplanar-matriz.py
# Aplanar una matriz de 2 dimensiones a una lista de 1 dimensión usando comprensión de listas
print("\033[2J\033[H", end="")
print("\033[1;34m"+"Aplanar una matriz de 2 dimensiones a una lista de 1 dimensión" + "\033[0m")
matriz = [[1, 2, -3], [4, -5, 6], [-7, 8, 9]]
# Aplanar la matriz a una lista de 1 dimensión usando comprensión de listas
lista_aplanada = [elemento for fila in matriz for elemento in fila]
positivos = [x for x in lista_aplanada if x > 0]
negativos = [x for x in lista_aplanada if x < 0]
print("Matriz original:", matriz)
print("Lista aplanada:", lista_aplanada)
print("Números positivos:", positivos)
print("Números negativos:", negativos)
