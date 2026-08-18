# p002-area-circulo.py
# Calcular el area de un circulo
import math # importa la libreria de constantes y funciones matematicas
print("\033[2J\033[H", end="")
print ("calculando el area de un circulo \n ")

radio = float(input("ingresa el radio del circulo "))

area= math.pi * radio ** 2
print (f"el radio del circulo es {radio} y el area es {area:.2f}")
