# p098-cuadrados-lista.py
# Generar cuadrados usando comprension de listas
print("\033[2J\033[H", end="")
print("Generar cuadrados desde 1 hasta n usando comprension de listas \n")
n = int(input("Ingrese un número entero positivo n: "))
numeros = list(range(1, n + 1))
cuadrados = [x**2 for x in range(1, n + 1)]
print("Números del 1 al", n, ":", numeros)
print("Cuadrados de los números del 1 al", n, ":", cuadrados)