# p015-hipotenusa-triangulo.py
# Calcular la hipotenusa de un triangulo rectangulo
import math as mt
print("\033[2J\033[H", end="")
print("Calcular la hipotenusa de un triangulo rectangulo \n")
cateto1 = float(input("dame el valor del cateto 1: "))
cateto2 = float(input("dame el valor del cateto 2: "))
hipotenusa = mt.sqrt(mt.pow(cateto1,2)+ mt.pow(cateto2,2))
print(f"El cateto 1 es: {cateto1}")
print(f"El cateto 2 es: {cateto2}")
print(f"La hipotenusa es: {hipotenusa:.3f}")