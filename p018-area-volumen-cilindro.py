# p018-area-volumen-cilindro.py
# Crea un programa que calcule el área y volumen de un cilindro. Pide al usuario que ingrese el radio y la altura
# del cilindro.
import math as mt
print("\033[2J\033[H", end="")
print("Calcular el área y volumen de un cilindro \n")
radio = float(input("dame el valor del radio: "))
altura = float(input("dame el valor de la altura: "))
area = 2 * mt.pi * radio * (radio + altura)
volumen = mt.pi * mt.pow(radio, 2) * altura
print(f"El radio es   : {radio} cm")
print(f"La altura es  : {altura} cm")
print(f"El área es    : {area:.3f} cm²")
print(f"El volumen es : {volumen:.3f} cm³") 