# p047-conteo-descendente-v2.py
# Imprimir los numeros de 100 a 1
print("\033[2J\033[H", end="")
print("Imprimir decendente deseado por el usuario.")
i = int(input("Dame el numero inicial de la secuencia decendente:...."))
paso = int (input("Dame el paso de la secuencia decendente:...."))
while i >= 1:
    print(i, end=" ")
    i -= paso
print ("\n Proceso terminado...")
