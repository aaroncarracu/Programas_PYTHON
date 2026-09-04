# p061-suma-200.py
# Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos
# números se introdujeron y la suma final.
while True:
    print("\033[2J\033[H", end="")
    print("Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200")
    suma = 0
    conteo = 0
    while suma <= 200:
        print(f" suma actual: {suma}")
        n = int(input("Numero: "))
        suma += n
        conteo += 1
    print(f"\n Se introdujeron {conteo} números")
    print(f" Suma final: {suma}")
    if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break
                
print("\n Proceso terminado...")  