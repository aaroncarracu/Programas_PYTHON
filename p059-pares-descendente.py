# p059-pares-descendente.py
# Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el
# usuario.
while True:
    print("\033[2J\033[H", end="")
    print("Imprimir los números pares y su suma total en un rango descendente desde 100")
    n = int(input("Ingrese un número entero positivo: (Menor a 100) "))
    suma = 0
    i = 100
    while n <= i:
        if i % 2 == 0:
            print(f"{i}", end=" ")
        suma += i
        i -= 1
    print(f"\nLa suma total de los números pares es: {suma}")
    if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break
        
print("\n Proceso terminado...")  