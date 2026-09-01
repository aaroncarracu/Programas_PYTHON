# p044-conteo-ascendente.py
# Escribe un programa que utilice un ciclo while para mostrar en pantalla una secuencia ascendente.
print("\033[2J\033[H", end="")
print("Escribe un programa que utilice un ciclo while para mostrar en pantalla una secuencia ascendente.")
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1
print ("\n Proceso terminado...")
