# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla de multiplicar de un numero dado
while True :
     
     print("\033[2J\033[H", end="")
     print("Imprimir tabla de multiplicar \n")
     n = int(input("Que tabla quieres? "))
     f = int(input("Hasta que numero quieres multiplicar? "))

     print("\n Imprimiendo la tabla del " + str(n))
     i = 1
     while i <= f:
        print(f"{n} x {i} = {n * i}")
        i += 1
     if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break

print("\n Proceso terminado...")  