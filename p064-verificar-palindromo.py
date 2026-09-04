# p064-verificar-palindromo.py
# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se
# lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).
while True:
    print("\033[2J\033[H", end="")
    print("Verificar si un número es palíndromo")
    n = int(input("Introduce un número entero: "))
    orig =n
    inv = 0
    while n > 0:
        dig = n % 10
        inv = inv*10 +dig
        n = n // 10
        print(f"{dig}")
    if inv == orig:
        print(f"\n{orig} es un palíndromo.")
    else:
        print(f"\n{orig} no es un palíndromo.")
    if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break
                        
print("\n Proceso terminado...")  
