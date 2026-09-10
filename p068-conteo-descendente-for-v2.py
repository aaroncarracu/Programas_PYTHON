# p068-conteo-descendente-for-v2.py
# Imprime numeros desde n a 1 con decrementos de m con un for
print("\033[2J\033[H", end="")
print("Imprime numeros desde n a 1 con decrementos de m con un for ")
n = int(input("Dame el valor de n maximo: "))
m = int(input("Intervalos: "))
for i in range (n, 0,-m) :
    print(i, end=" ")
print("\n Proceso terminado...")