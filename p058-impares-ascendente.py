# p058-impares-ascendente.py
# Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el
# usuario.
while True:
    print("\033[2J\033[H", end="")
    print("Imprimir los números impares y su suma total en un rango ascendente desde")
    n = int(input("Ingrese un número entero positivo: "))
    suma = 0
    i = 0
    while i <= n:
        
        if i % 2 != 0:
          print(f"{i}", end=" ") 
        suma += i
        i += 1
    print(f"\nLa suma total de los números impares es: {suma}")
    if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break
    
print("\n Proceso terminado...")  

     
           

   
