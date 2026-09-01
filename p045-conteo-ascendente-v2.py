# p045-conteo-ascendente-v2.py
# Escribe un programa que utilice un ciclo while para mostrar en pantalla una secuencia ascendente.
print("\033[2J\033[H", end="")
print("Escribe un programa que utilice un ciclo while para mostrar en pantalla una secuencia ascendente.")
i = 1
f = int(input("Dame el numero final de la secuencia:...."))
paso = int(input("Dame el paso de la secuencia:...."))
while i <= f:
    print(i, end=" ")
    i += paso
print ("\n Proceso terminado...")