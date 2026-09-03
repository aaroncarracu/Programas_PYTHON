# p052-tabla-conversion.py
# Imprime una tabla de conversion de peso a dolar 
while True:
  print("\033[2J\033[H", end="")
  print("Tabla de conversion de peso a dolar ")
  tc = 16.98 # tipo de cambio actual
  print(f"Tipo de cambio: {tc}")
  print("-"*40)
  while True : # Validacion de los datos de entrada 

    inicial = float(input("Dame el valor inicial: "))
    final = float(input("Dame el valor final    : "))
    if inicial < final and inicial > 0 and final > 0: break 
    else : print("El valor final debe de ser mayor al incial")


  c= inicial
  print("\nPeso\t\tDolar")
  print("-"*30)

  while c <= final:
     print(f"{c:10.2f} \t{c/tc:10.2f}")       
     c += 1
  print("-"*30)
  if input("\nDeseas hacer otra conversion? (S/N): ").upper() == "N":
    break
print("\n Proceso terminado...")

