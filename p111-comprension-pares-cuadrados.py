# p111-comprension-pares-cuadrados.py
# Generar una lista de números enteros del 1 al n (donde n es ingresado por el usuario). Utilizando comprensión de
# listas, obtener una nueva lista que contenga los cuadrados únicamente de los números pares. Imprimir la lista con
# el rango completo, la lista resultante de cuadrados y la suma de dichos cuadrados.
# Pedir el valor de n al usuario
print("\033[2J\033[H", end="")
n = int(input("Ingresa un número entero n: "))

# Generar la lista de números del 1 al n
lista = [x for x in range(1, n + 1)]

# Obtener los cuadrados de los números pares
cuadrados = [x**2 for x in lista if x % 2 == 0]

# Calcular la suma de los cuadrados
suma = sum(cuadrados)

# Imprimir los resultados
print("Lista completa:", lista)
print("Cuadrados de los números pares:", cuadrados)
print("Suma de los cuadrados:", suma)