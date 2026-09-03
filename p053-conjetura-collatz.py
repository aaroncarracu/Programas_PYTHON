# p053-conjetura-collatz.py
# Imprime la conjetura de collatz 
# Dado n, si n es par, se divide entre 2, si es impar se multiplica por 3 y se suma 1.

while True:
   print("\033[2J\033[H", end="")
   print("Conjetura de collatz \n")
   n = int(input("Dame un numero entero positivo: "))
   while n != 1:
      
      print(f"{n}", end=" ")
      if n % 2 == 0:
         n = n // 2
      else:
         n = 3 * n + 1
   print(n)
   if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N": break
   
   print("\n Proceso terminado...")  