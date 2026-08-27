# p034b-tipo-angulo.py
# Dado un angulo de 0 a 360 indicar que tipo de angulo es 
print("\033[2J\033[H", end="")
print("Dado un angulo de 0 a 360 indicar que tipo de angulo es: \n")

ang = int (input("Dame angulo: "))

if ang < 0 or ang > 360 :
  print("\nEl angulo esta fuera de rango") 
else :
 print("Tu angulo es : ", end="")
 if ang < 90 : print("Es agudo")
 elif ang == 90 : print("Es recto")
 elif ang < 180 : print("Es obtuso")
 elif ang == 180 : print("Es llano")
 elif ang < 360 : print("Es concavo")
 elif ang == 360 : print("Es cerrado")



print("\nProceso terminado") 