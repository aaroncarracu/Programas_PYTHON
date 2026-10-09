# p109-lista-impares.py
# Leer un entero n. Llenar una lista con los primeros n números impares.
print("\033[2J\033[H", end="")
lista=[]
while True:
    numero = input("dame un numero n (o ' ' para terminar): ")
    if numero == ' ':
        break
    elif int(numero) % 2 != 0:
       lista.append(int(numero))
    else:
        print("numero no es impar")

print(f"La lista es: {lista}")
suma=prom=0
for X in lista :
    suma+= X
prom= suma / len(lista)
print(f"la suma es: {suma}")
print(f"El promedio es: {prom}")

# 2. Números divisibles entre 3 y su suma
divisibles = []
suma_divisibles = 0

for X in lista:
    if X % 3 == 0:
        divisibles.append(X)
        suma_divisibles += X

print(f"Números divisibles entre 3: {divisibles}")
print(f"La suma de los divisibles entre 3 es: {suma_divisibles}")

# 3. Buscar un elemento y mostrar su índice
buscar = int(input("Ingresa el número que deseas buscar: "))

if buscar in lista:
    print(f"El número {buscar} sí está en la lista")
    print(f"Su índice es: {lista.index(buscar)}")
else:
    print(f"El número {buscar} no está en la lista")