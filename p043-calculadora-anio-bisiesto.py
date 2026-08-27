# p043-calculadora-anio-bisiesto.py
# Escribe un programa que determine si un año, ingresado por el usuario, es bisiesto. Un año es bisiesto
# si cumple una de las siguientes condiciones:
print("\033[2J\033[H", end="")
print("Escribe un programa que determine si un año es bisiestro")
año = int (input("Dame el año: "))

if año % 4 ==  0 :
    print(f"El año {año} es bisiesto.")
elif año % 400 == 0:
    print(f"El año {año} es bisiesto.")
elif año % 100 == 0 :
    print(f"El año {año} no es bisiesto.")
else :
    print(f"El año {año} no es bisiesto.")
print("\n El proceso termino....")
      