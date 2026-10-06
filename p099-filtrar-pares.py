# p099-filtrar-pares.py
# Filtrar números pares de una lista usando comprensión de listas
print("\033[2J\033[H", end="")
print("Filtrar números pares de una lista usando comprensión de listas \n")
cant = int(input("Ingrese la cantidad de números que desea ingresar: "))
numeros =[]
# introduce los números en la lista
for i in range(cant):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)
# se filtran los numeros pares e impares usando comprensión de listas
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
print("Números ingresados:", numeros)
print(f"Números pares: {pares} - Cantidad de pares: {len(pares)}")
print(f"Números impares: {impares} - Cantidad de impares: {len(impares)}")