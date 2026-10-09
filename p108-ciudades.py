# p108-ciudades.py
# Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $.
print("\033[2J\033[H", end="")
ciudades = []
while True:
    ciudad = input("Ingrese el nombre de una ciudad (o '$' para terminar): ")
    if ciudad == '$':
        break
    ciudades.append(ciudad)

# ● Cuántos elementos tiene la lista.
# ● La lista completa.
# ● La lista ordenada en orden descendente.
# ● Cuántas ciudades inician con una letra consonante y sus nombres.

print(f"La lista tiene {len(ciudades)} elementos.")
print(f"La lista completa es: {ciudades}")
# ordenar cuidades de z a a a
ordenadas = sorted(ciudades, reverse=True)
print(f"Ciudades ordenadas: {ordenadas}")


consonantes = "bcdfghjklmnpqrstvwxyz"
contador = 0
ciudades_consonante = []

for ciudad in ciudades:
    if ciudad[0].lower() in consonantes:
        contador += 1
        ciudades_consonante.append(ciudad)

print(f"Hay {contador} ciudades que inician con una letra consonante.")
print(f"Las ciudades que inician con una letra consonante son: {ciudades_consonante}")
