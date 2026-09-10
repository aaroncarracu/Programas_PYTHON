# p069-arriba-abajo.py
# imprime numeros de n a 1 o de 1 a n segun lo decidas
print("\033[2J\033[H", end="")
print("imprime numeros de n a 1 o de 1 a n segun lo decidas")
print("[!] voy de 1 a n")
print("[2] voy de n a 1")
op = int(input("Elige? "))
if op == 1:
  print("Vamos hacia arriba de 1 hasta n")
  n = int (input("Dame el valor de n: "))
  for i in range(1, n+1):
    print(i, end=" ")
elif op == 2:
  print("Vamos hacia abajo de n hasta 1")
  n = int (input("Dame el valor de n: "))
  for i in range(n,0,-1):
    print(i, end=" ")
else: 
    print("\n respuesta incorrecta")
print("\n Proceso terminado..... ")
 