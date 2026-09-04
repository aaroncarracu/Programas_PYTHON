# p060-promedio-suma.py
# Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la
# suma y el promedio de la serie.
while True:
    print("\033[2J\033[H", end="")
    print("Leer números introducidos por el usuario hasta que ingrese un 0, mostrar conteo,suma y promedio")
    prom= 0
    suma = 0
    conteo = 0
    while True:
        n = int(input("Numero: (0 para terminar) "))
        if n == 0: break
        else:
            suma += n
            conteo += 1
    prom = suma /conteo
    print(f"\n Se introdujeron {conteo} números")
    print(f" Suma total: {suma}")
    print(f" Promedio: {prom:.2f}")
    if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break
            
print("\n Proceso terminado...")  
