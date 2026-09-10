# p066-conteo-ascendente-for-v2.py
# Numeros de 1 a n con intervalos de m usando for
print("\033[2J\033[H", end="")
print("Numeros de 1 a n con intervalos de m usando for ")
n = int(input("Dame el valor de n maximo: "))
m = int(input("Intervalos: "))
for i in range (1, n+1,m) :
    print(i, end=" ")
print("\n Proceso terminado...")