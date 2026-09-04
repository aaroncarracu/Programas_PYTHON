# p063-numero-mayor.py
# Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el
# número más grande de todos los introducidos.
while True :
    print("\033[2J\033[H", end="")
    print("Leer una serie de números hasta que el usuario ingrese un 0,  imprimir el mayor")
    mayor = 0
    while True:
        n = int(input("Numero: (0 para terminar) "))
        if n == 0: break
        elif n > mayor:
            mayor = n
    print(f"El número más grande es: {mayor}")
    if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break
print("\n Proceso terminado...")