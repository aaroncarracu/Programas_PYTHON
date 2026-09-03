# p055-tabla-multiplicar-while-v2.py
# Imprime todas tablas del 1 al 10

while True :
    print("\033[2J\033[H", end="")
    print("Imprimir tablas de multiplicar 1 al 10 \n")

    f = int(input("Hasta que tabla quieres: "))
    fl = int(input("Hasta donde llaga: "))
    n = 1
    while n <= f:
        print(f"\nTabla del {n}:")
        i = 1
        while i <= fl:
            print(f"{n} x {i} = {n * i}")
            i += 1
        n += 1
    if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break

print("\n Proceso terminado...")  